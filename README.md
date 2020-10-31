# Post File Server

A simple HTTP server capable of receiving files and saving them to designated directory.

## API

```
POST /api/upload_log
Content-Type: multipart/form-data
<form><input type="file" name="file">{file_name}</input></form>
```

CURL example:
```bash
$ curl -X POST -F "file=@test.log" localhost:5000/api/upload_log
```

## Usage

Prerequisites: Docker, Bash.

1. Checkout repository.
2. Run `build.sh` to build docker image.
3. Run `run.sh` to start server.

Note that `run.sh` has command line arguments that allow to specify **port** and **output directory**.
Use `run.sh --help` to see the details.
