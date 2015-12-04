#sh

for FILE in `ls results | grep ".extrinseque"`
do
  echo "${FILE}  (Relevant) : `grep "Relevant" "results/${FILE}" | wc -l` / `grep "elevant" "results/${FILE}" | wc -l`"
done


