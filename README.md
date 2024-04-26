# HLS Video Streaming Server

This project demonstrates a simple HLS (HTTP Live Streaming) server built with Python and Flask. The server hosts video content split into chunks and a playlist file, enabling seamless video streaming over HTTP.

## Requirements

- Python 3.6 or higher
- Flask
- ffmpeg (for preparing the HLS content)

## Setup

### Step 1: Install Dependencies

Ensure you have Python installed on your system. Then, install the required Python packages using pip:

```bash
pip install flask
```

### Step 2: Prepare Video Content

Before running the server, you need to prepare your video files in HLS format. You can use ffmpeg to convert a regular video file into the necessary format. Here's how to do it:

```bash
ffmpeg -i video/a.mp4 -profile:v baseline -level 3.0 -s 640x360 -start_number 0 -hls_time 10 -hls_list_size 0 -f hls video/index.m3u8
```

This command will create a series of `.ts` video segments and an `index.m3u8` playlist file inside the `video` directory of your project.

### Step 3: Place Video Content

Ensure that the generated `.ts` files and `index.m3u8` file are located in the `video` directory within your project folder. If not, move them there or adjust the `MEDIA_FOLDER` path in the application to match the location of these files.

## Running the Server

To run the server, navigate to the project directory in your terminal and execute the following command:

```bash
python ffpmeg.py
```

This command will start the Flask server on `localhost` at port `5000`.

## Accessing the Stream

To access the stream:
- Open a video player that supports HLS (like VLC).
- Choose to open a network stream and enter the URL: `http://localhost:5000/video/index.m3u8`

You should now be able to watch the video being streamed from your local server.

## Notes

This setup is intended for development and testing purposes. For production use, consider implementing additional features like authentication, logging, error handling, and possibly using a more robust web server like Nginx or Apache to serve the static files.

