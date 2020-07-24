# The observer package

## Table of Contents
* [Introduction](#introduction)
* [Technology](#technology)
* [Features](#features)
* [Install](#install)
* [Usage](#usage)

## Introduction
With the observer class you can handle an arbitrary number of ROS subscriber nodes at ones. I wrote it to enhance the quality of live while writing ROS Nodes which rely on the output of multiple subscriber nodes at ones. The observer requests the message type and remaps so you just have to know the names of the topics you want to subscribe to.

#### Keywords
#ROS #Subscriber #Python

## Technology
* Python 3
* ROS Kinetic Kame
* ROS Noetic Ninjemys

## Features
* Create multiple subscribers of arbitrary number with only the names of the topics.
* Get the latest message of a specific subscriber.
* Get the point in time when the latest message was received of a specific subscriber.

## Install
Copy the package into the ```src``` folder of your catkin workspace and call ```catkin_make```out of the main folder in your the catkin workspace.

## Usage
Import the observer class:
```
from observer.Observer import Observer
```

Create the observer with a list of topic names:
```
topic_list = ["topic_name_1", "topic_name_2"]
observer = observer(topic_list)
```

Get the latest message of a specific topic:
```
message = observer.get_message("topic_name_1")
```
Get the point in time of a latest message:
```
point_in_time = observer.get_update_time("topic_name_1")
```

## License
Copyright <2020> <Alexander König>

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
