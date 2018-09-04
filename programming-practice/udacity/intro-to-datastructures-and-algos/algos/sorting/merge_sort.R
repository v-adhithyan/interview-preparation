library(ggplot2)
chunk <- function(x,n){
  numOfVectors <- floor(length(x)/n)
  elementsPerVector <- c(rep(n,numOfVectors-1),n+length(x) %% n)
  elemDistPerVector <- rep(1:numOfVectors,elementsPerVector)
  split(x,factor(elemDistPerVector))
}

merge.sort <- function(array) {
  mid = as.integer(length(array) / 2)
  
}

main <- function() {
  input <- c(10, 4, 3, 5, 1, 7, 6, 2, 8, 9)
  
  
  input <- c(10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
  #input <- round(runif(10,1,100), 0)
  barplot(input, main="Merge Sort Visualization")
  merge.sort(input)
}

main()
