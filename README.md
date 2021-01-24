# Transcoder

This repository contains a Python 3 script, `transcode.py`, that takes
a mapping CSV and some input text and prints the text out with
characters randomly replaced according to the given mapping.

The instructions here assume that the user's running Mac OS X.

## Setup Python 3

Since it's a Python 3 script, we need Python 3 installed on the
computer where it's to be run.

So, head to https://www.python.org and download the latest version and
use the graphical installer to install Python 3. As of now, the latest
version is Python 3.9.1, but it doesn't matter as long as it's above
3.

## Download the script

Open Terminal. You can do this by pressing the [Command] key and
[Spacebar] together and typing in "terminal".

Type the following into the terminal, ignoring the `$` sign:

```
$ git clone git@github.com:hidemin1225/cyberpunk_tomorrow.git
```

You should see the following output:

```
Cloning into 'cyberpunk_tomorrow'...
remote: Enumerating objects: 14, done.
remote: Counting objects: 100% (14/14), done.
remote: Compressing objects: 100% (12/12), done.
remote: Total 14 (delta 1), reused 8 (delta 0), pack-reused 0
Receiving objects: 100% (14/14), done.
Resolving deltas: 100% (1/1), done.
```

Then, enter the `cyberpunk_tomorrow` directory by entering the following command:

```
$ cd cyberpunk_tomorrow
```

Now, you're inside the `cyberpunk_tomorrow` directory.

To test, run the following command:

```
$ ./transcode.py
```

You should see the following output:

```
Usage:

./transcode.py [path-to-mapping-csv] [one-in-how-many] < [path-to-input-text-file] > [path-to-output-text-file]

one-in-how-many: if given, say 10, 1 in 10 characters will be transcoded

```

## Running the script

To run the script, you need to additional files:
1. The mapping CSV
2. The input text file

To make testing easier, we provide a sample mapping CSV and a sample
input text file in the repository. In "production" use, you should use
your own mapping CSV and input text file.

If you only want to test the
script interactively, with any random input from the keyboard, you
only need the mapping CSV.

### Interactive mode

Run the script like so:

```
$ ./transcode.py sample_mapping.csv 10
```

Then, the script will be waiting for input from the keyboard. Say, we
type the following and press the [Return] key:

```
Hi, I'm testing the transcoder for Cyberpunk Tomorrow!
```

You should then see something like this on the screen:

```
Hi, I'm teֆπing thⓔ transcoder for Cyberpunʞ Tomorrøw!
```

The script will _not_ exit after this and will keep waiting for
further input from the keyboard to transcode.

To exit, press the [Control/Ctrl] key and the [d] key at the same
time.

Note that the number `10` in the command above means that `1` in `10`
characters will be transcoded. You can specify a smaller or bigger
number to dial the rate of transcoding up or down, respectively.

### Batch mode

To process an entire input text file, run the script like so:

```
$ ./transcode.py sample_mapping.csv 10 < romeo-and-juliet.txt
```

The script should then print the contents of file, but transcoded, on to the
screen and exit.

To save the output to another file, run the script like so:

```
$ ./transcode.py sample_mapping.csv 10 < romeo-and-juliet.txt > output.txt
```

Then type the following into Terminal:

```
$ open output.txt
```

It should open the output file in TextEdit or whatever default
application is configured for text files.
