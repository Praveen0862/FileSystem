Here are Sample testcases for executing


ls

mkdir user

cd user

mkdir projects

touch projects/me.txt

cat projects/me.txt

cd projects

echo "I am Praveen" > me.txt

cat me.txt

cd ../..

mkdir guest/projects

mv user/projects/me.txt ./guest/projects

cd guest/projects

cat me.txt

echo "I am guest" > me.txt

cd ../../praveen/projects

cp ../../guest/projects/me.txt

