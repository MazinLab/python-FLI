import FLI

cams = FLI.USBCamera.find_devices()
cam0 = cams[0]
print("info:", cam0.get_info())
print("image size:", cam0.get_image_size())
print("temperature:", cam0.get_temperature())
print("mode:", cam0.get_camera_mode_string())
cam0.set_image_binning(2, 2)
cam0.set_bitdepth("16bit")  # this should generate a warning for any USB camera in libfli-1.104
cam0.set_exposure(5)
img = cam0.take_photo()
print(img)