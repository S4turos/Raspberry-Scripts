#!/bin/bash

vcgencmd measure_temp | tr -dc '[. [:digit:]]'
