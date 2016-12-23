
for fold in $(find . -type d -regextype posix-extended -regex '.*week-[0-9]{1}')
do
    echo $fold
    mv $fold '${file:0:4}0${file:4:1}'; 
done
