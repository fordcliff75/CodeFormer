import torch
import numpy as np
import cv2

def tensor2img_fast(tensor, rgb2bgr=True, min_max=(0, 1)):
    output = tensor.squeeze(0) if tensor.dim() == 4 else tensor
    output = output.detach().clamp_(*min_max).permute(1, 2, 0)
    output = (output - min_max[0]) / (min_max[1] - min_max[0]) * 255
    output = output.round().type(torch.uint8).cpu().numpy()
    if output.shape[-1] == 1:  # gray image
        output = np.squeeze(output, axis=2)
    else:
        if rgb2bgr:
            output = cv2.cvtColor(output, cv2.COLOR_RGB2BGR)
    return output

# 4D 3-channel
t1 = torch.rand(1, 3, 10, 10)
out1 = tensor2img_fast(t1)
print(out1.shape)

# 3D 3-channel
t2 = torch.rand(3, 10, 10)
out2 = tensor2img_fast(t2)
print(out2.shape)

# 4D 1-channel
t3 = torch.rand(1, 1, 10, 10)
out3 = tensor2img_fast(t3)
print(out3.shape)

# 3D 1-channel
t4 = torch.rand(1, 10, 10)
out4 = tensor2img_fast(t4)
print(out4.shape)

print("All tests passed.")
