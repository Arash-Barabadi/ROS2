# Measurement of messsage transport rate
## in this section we are checking the way to measre the lag of data tranformation rate;

### if you have a very high publish rate and you see that message are not quickly enough, then maybe you can see that the rate would be dropped. For checking the rate, the following command should be written: 
```bash
ros2 topic hz /robot_news
```
### or for band width;
```bash
ros2 topic bw /robot_news
```
