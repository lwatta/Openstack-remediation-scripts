# to copy the files
for file in *; do cp $file ${file/#svl11/svl12}; done

# change internals of the file
find ./ -name "svl12*" -print0 | xargs -0 -I {}  sed -i -e 's/svl11/svl12/g' {}

find ./ -name "svl12*" -print0 | xargs -0 -I {}  sed -i -e 's/cloud-11/cloud-12/g' {}
