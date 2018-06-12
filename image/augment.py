import cv2


def resize(src, width, height, interpolation='CV_INTER_NEAREST'):
	"""
	Resizes the image src down to or up to the specified size.

	Args:
		src - input image.
		weight(int) - number of columns.
		height(int) - number of rows.
		interpolation(str)- resample method.
			
			interpolation methods:
			INTER_NEAREST - a nearest-neighbor interpolation (used by default)
			INTER_LINEAR - a bilinear interpolation (used by default in cv2)
			INTER_AREA - resampling using pixel area relation. It may be a preferred method for image decimation, 
				as it gives moire’-free results. But when the image is zoomed, it is similar to the INTER_NEAREST method.
			INTER_CUBIC - a bicubic interpolation over 4x4 pixel neighborhood
			INTER_LANCZOS4 - a Lanczos interpolation over 8x8 pixel neighborhood

		help-https://docs.opencv.org/2.4/modules/imgproc/doc/geometric_transformations.html#resize

	Return:
		resized image.
	"""
	return cv2.resize(src, (width, height), interpolation)