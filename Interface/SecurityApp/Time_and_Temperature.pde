void displayTT(){
   textFont(font2);
fill(0);
text( ( year() + "-"+nf(month(),2) +"-"+ nf(day(),2) + "--"  + nf(hour(),2) +"-"+ nf(minute(),2) +"-"+ nf(second(),2)),1000,25);
//println(loadStrings("https://weather.yahoo.com/"));
}