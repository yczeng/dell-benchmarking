# dell-benchmarking

Documentation for how to do deep learning benchmarking with TensorRT v2 with the giexec module.

## Download programs
Download cuda & follow instructions to install:
https://developer.nvidia.com/cuda-downloads

Install TensorRT v2:
https://developer.nvidia.com/tensorrt

Install PuTTY to ssh into Dell servers:
http://www.putty.org/

## Benchmarking with giexec module

cd into the correct folder to do benchmarking giexec:
```
cd /usr/src/gie_samples/samples/giexec
```

make the program:
```
sudo make all
```
cd into the correct folder to run the program.
```
cd /usr/src/gie_samples/samples
```
to see the help screen:
```
./bin/giexec
```
### Benchmarking with GoogLeNet 
GoogLeNet is already contained within the TensorRT program. You want to run benchmarking with int8, and "output=prob" while varying the batch size as needed.
To run with batchsize=1:
```
./bin/giexec --model=data/samples/googlenet/googlenet.caffemodel --deploy=data/samples/googlenet/googlenet.prototxt --output=prob --int8 --batch=2
```
### Benchmarking with AlexNet
Download the `bvlc_alexnet.caffemodel` and `deploy.prototxt` file from [here](https://github.com/yczeng/dell-benchmarking), and save it into a folder you make and name `alexnet`, which you move into `/usr/src/gie_samples/samples/data/samples`.

Make sure you're in the correct folder: `/usr/src/gie_samples/samples`

Same as for googLeNet, you want to run benchmarking with int8 and "output=prob" while varying the batch size as needed.
To run with batchsize=1:
```
./bin/giexec --model=data/samples/alexnet/bvlc_alexnet.caffemodel --deploy=data/samples/alexnet/deploy.prototxt --output=prob --int8 --batch=1
```
### Benchmarking with multiple GPUs in the server setup
Change line 13 in `Makefile.giexec` from "CC = g++" to "CC = mpicxx"

Download Open MPI: https://www.open-mpi.org/software/ompi/v2.1/

Replace the old `giexec.cpp` file with the one contained in the repo.

To run, add `mpirun -np 4`, replacing 4 with the number of GPUs in your server setup, in front of the commands starting with `./bin/giexec/` listed above.

## Converting data to images per second
Copy and paste output in a text file with the times separated by the batch file. See `AlexNetData` as a sample file for format.
Run the python script `processdata.py` to have times per run automatically converted to images/sec.

You'll want to make sure that the AlexNet data is saved in a file called `AlexNetData` and the GoogLeNet data is saved in a file called `GoogLeNetData`, and update line 2 in the script to reflect where you've stored these files.

Or otherwise, just update 2, 37, and 38 as needed.
