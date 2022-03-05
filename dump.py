#!/usr/bin/python3
import os
import aiml

BRAIN_FILE = "brain.dump"

k = aiml.Kernel()
print("Parsing aiml files")
k.bootstrap(learnFiles="std-startup.aiml", commands="load aiml b")
print("Saving brain file: " + BRAIN_FILE)
k.saveBrain(BRAIN_FILE)
