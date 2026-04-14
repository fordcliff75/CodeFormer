## 2024-05-24 - Video Frame Buffering Optimization
**Learning:** Loading all video frames into a python list before writing them out via cv2/VideoWriter leads to immense memory usage and easily causes OOM crashes for even moderately sized videos.
**Action:** Stream video frames directly from the filesystem (or generator) into the `VideoWriter` one at a time, keeping the memory footprint at O(1) instead of O(N).
