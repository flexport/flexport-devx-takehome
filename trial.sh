#name= "ASHWIN"
#my_var= "echo $name" | awk '{print tolower($0)}'

y="HeLlo/"
echo $y
val=$(echo $y | tr '[:upper:]' '[:lower:]')
echo $val
