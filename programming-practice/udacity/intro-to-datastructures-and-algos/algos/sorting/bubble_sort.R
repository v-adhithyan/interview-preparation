swap <- function(i, j, data) {
  temp <- data[i]
  data[i] <- data[j]
  data[j] <- temp
  return data
}

sleep <- function() {
  current_time <- Sys.time()
  while(as.numeric(Sys.time()) - as.numeric(current_time) < 0.5) {}
}

input <- c(10, 4, 3, 5, 1, 7, 6, 2, 8, 9)
barplot(input)

for(i in 1:length(input)) {
  j = i + 1
  while(j <= length(input)) {
    if(input[i] > input[j]) {
      input <- swap(i, j, input)
      barplot(input)
    }
    j = j + 1
    sleep()
  }
}