

sleep <- function() {
  current_time <- Sys.time()
  while(as.numeric(Sys.time()) - as.numeric(current_time) < 0.2) {}
}

bubble_sort <- function(input) {
  for(i in 1:length(input)) {
    j = i + 1
    while(j <= length(input)) {
      if(input[i] > input[j]) {
        temp <- input[i]
        input[i] <- input[j]
        input[j] <- temp
        barplot(input, main="Bubble Sort Visualization")
      }
      j = j + 1
      sleep()
    }
  }
}

main <- function() {
  input <- c(10, 4, 3, 5, 1, 7, 6, 2, 8, 9)
  
  
  input <- c(10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
  #input <- round(runif(10,1,100), 0)
  barplot(input, main="Bubble Sort Visualization")
  bubble_sort(input)
}

main()
