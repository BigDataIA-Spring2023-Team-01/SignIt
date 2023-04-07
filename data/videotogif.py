import cv2
import glob
import time

# Define the path to the video files
video_path = "data/misseddataset"

# Define the path to the output gif file
gif_path = "data/kaggledataset/gifs"

# Define the number of frames per second for the gif
fps = 10

# Define the width and height of the gif
width = 640
height = 480

# Create a list of all the video files
video_files = glob.glob(video_path + "/*.mp4")

# Start the timer
start_time = time.time()

# Iterate through the video files
for video_file in video_files:

    # Load the video file
    video = cv2.VideoCapture(video_file)

    # Get the number of frames in the video
    num_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # Create a blank image for the gif
    gif_image = cv2.imread("blank.png")

    # Iterate through the frames in the video
    for frame_index in range(num_frames):

        # Get the current frame from the video
        frame = video.read()[1]

        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Resize the gray frame to the size of the gif image
        gray_frame = cv2.resize(gray_frame, (width, height))

        # Write the gif image to file
        cv2.imwrite(gif_path + "/frame_" + str(frame_index) + ".gif", gray_frame)

    # Release the video capture object
    video.release()

# Stop the timer
end_time = time.time()

# Print the total time taken
print("Total time taken:", end_time - start_time)