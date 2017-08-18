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
Download the `alexnet` folder in this git repo and move it into `/usr/src/gie_samples/samples/data/samples`.
Make sure you're in the correct folder: `/usr/src/gie_samples/samples`
Same as for googLeNet, you want to run benchmarking with int8 and "output=prob" while varying the batch size as needed.
To run with batchsize=1:
```
./bin/giexec --model=data/samples/alexnet/bvlc_alexnet.caffemodel --deploy=data/samples/alexnet/deploy.prototxt --output=prob --int8 --batch=1
```
