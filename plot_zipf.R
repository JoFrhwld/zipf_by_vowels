library(ggplot2)
library(plyr)

files = Sys.glob("by_*.txt")
read_zipf <- function(file){
  require(stringr)
  data = read.delim(file)
  seg = gsub(".txt", "", unlist(strsplit(file, "_"))[2])
  data$Seg = seg
  return(data)
}


data <- ldply(files, read_zipf, .progress = "text")

ggplot(data, aes(log(Rank), log(Freq), color = Seg))+
  geom_point()