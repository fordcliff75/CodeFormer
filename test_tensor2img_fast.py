import torch
import numpy as np

# Mock cv2 to avoid dependency issues in this test
class MockCV2:
    COLOR_RGB2BGR = 0
    @staticmethod
    def cvtColor(src, code):
        # Dummy behavior for rgb2bgr, just reverses last axis
        return src[..., ::-1]

import sys
import types
mock_cv2 = types.ModuleType('cv2')
mock_cv2.COLOR_RGB2BGR = MockCV2.COLOR_RGB2BGR
mock_cv2.cvtColor = MockCV2.cvtColor
sys.modules['cv2'] = mock_cv2

from basicsr.utils.img_util import tensor2img_fast, tensor2img

def test_tensor2img_fast():
    # Test case 1: 4D tensor (e.g. from network output)
    t1 = torch.rand(1, 3, 256, 256)
    out1_fast = tensor2img_fast(t1, rgb2bgr=True)
    out1_slow = tensor2img(t1, rgb2bgr=True)
    assert out1_fast.shape == (256, 256, 3), f"Expected (256, 256, 3), got {out1_fast.shape}"
    assert out1_fast.dtype == np.uint8, f"Expected uint8, got {out1_fast.dtype}"
    # Small difference expected due to .round() vs truncation
    diff1 = np.abs(out1_fast.astype(np.float32) - out1_slow.astype(np.float32)).max()
    assert diff1 <= 1.0, f"Max difference is {diff1}"

    # Test case 2: 3D tensor
    t2 = torch.rand(3, 128, 128)
    out2_fast = tensor2img_fast(t2, rgb2bgr=False)
    out2_slow = tensor2img(t2, rgb2bgr=False)
    assert out2_fast.shape == (128, 128, 3), f"Expected (128, 128, 3), got {out2_fast.shape}"
    assert out2_fast.dtype == np.uint8, f"Expected uint8, got {out2_fast.dtype}"

    # Test case 3: 4D tensor with 1 channel (grayscale)
    t3 = torch.rand(1, 1, 64, 64)
    out3_fast = tensor2img_fast(t3, rgb2bgr=False)
    out3_slow = tensor2img(t3, rgb2bgr=False)
    assert out3_fast.shape == (64, 64, 1), f"Expected (64, 64, 1), got {out3_fast.shape}"

    print("All tests passed!")

if __name__ == '__main__':
    test_tensor2img_fast()
