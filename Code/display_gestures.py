import cv2, os, random
import numpy as np

def get_image_size():
	img = cv2.imread('gestures/0/100.jpg', 0)
	return img.shape

gestures = os.listdir('gestures/')
gestures.sort(key = int)
begin_index = 0
end_index = 5
image_x, image_y = get_image_size()

rows = len(gestures) // 5 + 1 if len(gestures)%5 != 0 else len(gestures) // 5
full_img = None
for _ in range(rows):
	col_img = None
	for j in range(begin_index, end_index):
		img_path = "gestures/%s/%d.jpg" % (j, random.randint(1, 1200))
		img = cv2.imread(img_path, 0)
		if np.any(img is None):
			img = np.zeros((image_y, image_x), dtype = np.uint8)
		col_img = img if np.any(col_img is None) else np.hstack((col_img, img))
	begin_index += 5
	end_index += 5
	full_img = (
		col_img if np.any(full_img is None) else np.vstack((full_img, col_img))
	)

cv2.imshow("gestures", full_img)
cv2.imwrite('full_img.jpg', full_img)
cv2.waitKey(0)
