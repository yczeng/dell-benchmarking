# dell-benchmarking

Documentation for how to do deep learning benchmarking with TensorRT v2

Download cuda & follow instructions to install:
https://developer.nvidia.com/cuda-downloads

Install TensorRT v2:
https://developer.nvidia.com/tensorrt

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
to run googlenet on one GPU with batch size=1:
```
./bin/giexec --model=data/samples/googlenet/googlenet.caffemodel --deploy=data/samples/googlenet/googlenet.prototxt --output=prob --int8 --batch=2
```
