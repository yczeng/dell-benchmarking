# dell-benchmarking

Documentation for how to do deep learning benchmarking with TensorRT v2 with the giexec module.

## Download programs
Download cuda & follow instructions to install:
https://developer.nvidia.com/cuda-downloads

Install TensorRT v2:
https://developer.nvidia.com/tensorrt

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
