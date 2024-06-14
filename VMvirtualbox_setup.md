# HOW TO SET UP VMWARE TO ACCOMPLISH MULTI COMPUTER OPERATION
## 1.Download oracal VM VitualBox

```bash
https://www.virtualbox.org/
```

## 2.Download Windows operating system
install the "Create Windows 10 installation media" to get the iso file
```bash
https://www.microsoft.com/en-us/software-download/windows10
```

## 3.Create new(n) instances of computer in VM Virtual box

click on new(N) and the directory of your previously downloaded iso file in the correct place,
and proceed.
allocate memory based on your needs. IN EXPERIENCE, WINDOWS take 20GB and ANACONDA and other packages needs 5GB, you need around 50GB to ensure smooth operation.


## 4.Open the instance

if there is any issue with that have to do with produce key click on storage and remove the two undefined disk.
Then reopen the instance.
Finish setting uo the windows computer.

## 5. Download ANACONDA or MINICONDA

base on the storage you allocate, download anaconda or miniconda(this will require less storage).
```bash
https://www.anaconda.com/download/success
https://docs.anaconda.com/free/miniconda/
```

## 6. Create and setup environment using environment.yml

open powershell prompt of conda and type
```bash
conda env create -f environment.yml
```

## 7. download the files nessasry in github and start running the code!
