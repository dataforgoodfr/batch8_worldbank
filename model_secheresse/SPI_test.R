library(SPEI)

## Precipitation data
ALL_PRECIP <- read.csv("~/datasets/precipitation/ALL_PRECIP.csv")



library(dplyr)

## for month
mois <- ALL_PRECIP %>% select(Statistics) %>%
  filter(!duplicated(Statistics))
month <- as.data.frame(c(1:nrow(mois)))
colnames(month) <- "mois"
mois <- cbind(mois, month)
mois <- mois[1:12,]


ALL_PRECIP <- ALL_PRECIP %>% left_join(mois, by= "Statistics")

#split(ALL_PRECIP, ALL_PRECIP$region)

# region
region <- ALL_PRECIP %>% select(region) %>%
  filter(!duplicated(region)) 

# test
df = ALL_PRECIP %>% filter(region == "Eastern Africa") %>%
  select(Year, mois, Rainfall....MM.) %>%
  group_by(Year, mois) %>% summarise(pluie = mean(Rainfall....MM.))
test <- spi(df$pluie, 3)
plot.spei(test)
summary(test)
class(test)
  a <- as.data.frame(test$fitted)
b <- list(test)


## Generating all
x <- region

for(i in 1:nrow(x)){ 
  data2 <- ALL_PRECIP 
  data3 <- subset(data2, region == x[i,])
  data3 <- data3 %>% select(Year, mois, region, Rainfall....MM.) %>%
    group_by(Year, mois, region) %>% summarise(pluie = sum(Rainfall....MM.))
  data3_spi <- data3
  data4 <- data3_spi <- spi(data3$pluie, 6)
  data4 <- as.data.frame(data4$fitted)
  names(data4) <- "SPI3"
  data_final <- bind_cols(data3, data4)
  reg = region
  assign(paste0("SubsetData",i), data_final, envir = .GlobalEnv)
  
}

                  
nrow(region)    

# Bind
pluie_spi_region <- do.call("rbind", list(SubsetData1, SubsetData2, SubsetData3, SubsetData5,SubsetData6, SubsetData7, SubsetData8, SubsetData9,
                      SubsetData10, SubsetData11, SubsetData12, SubsetData13, SubsetData14, SubsetData15 ,SubsetData16, SubsetData17,
                      SubsetData18, SubsetData19, SubsetData20, SubsetData21, SubsetData22, SubsetData23))


getwd()
write.csv(x = pluie_spi_region, file = "precip_spi6_region_01122020.csv")
