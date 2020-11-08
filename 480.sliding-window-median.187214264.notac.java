class Solution {
    
    public double[] medianSlidingWindow(int[] nums, int k) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(new Comparator<Integer>(){
            public int compare(Integer p1, Integer p2) {
                return p2 - p1;
            }
        });
        double[] res = new double[nums.length - k + 1];
        for (int i = 0; i < nums.length; i++) {

              if (maxHeap.isEmpty() || nums[i] < maxHeap.peek()) {
                maxHeap.offer(nums[i]);
              } else {
                minHeap.offer(nums[i]);
              }
            
            if (i - k >= 0) {
                if (nums[i-k] <= maxHeap.peek()) {
                    maxHeap.remove(nums[i-k]);
                } else {
                    minHeap.remove(nums[i-k]);
                }
            }

          while (minHeap.size() >= maxHeap.size() + 1) {  
            maxHeap.offer(minHeap.poll());
          }
          while (maxHeap.size() > minHeap.size() + 1) {
            minHeap.offer(maxHeap.poll());
          }
            
      // add result
      if (i >= k - 1) {
        res[i -k + 1] = maxHeap.peek();
      }

            
        }
        return res;
    }
    
    
}
