#!/bin/bash

cd /root/bv

dts=$(less d.txt)
refs=$(less rf.txt | shuf | sed -e ':a;N;$!ba;s/\n/,/g')
prxs=$(less px.txt | shuf | sed -e ':a;N;$!ba;s/\n/,/g')
IFS=', ' read -r -a dt <<< "$dts"
IFS=', ' read -r -a refe <<< "$refs"
IFS=', ' read -r -a prxe <<< "$prxs"


arrIN=(${dts//|/ })
dom=${arrIN[0]}
px=${arrIN[1]}
go=${arrIN[2]}

# echo "tespython3.8 crawl.py -t "$dom" -r "${refe[0]}" -p "$px
# echo "tes $dom $px"
# exit 0

tref=${#refe[@]}
tprx=${#prxe[@]}

if [ "$go" == "s" ]; then
	# echo "python3.8 crawl.py -t $dom -r ${refe[0]} -p $px"
	# python3.8 crawl.py -t "$dom" -r "${refe[0]}" -p "${prxe[0]}"
  python3.8 crawl.py -t "$dom" -r google -p "${prxe[0]}"
  python3.8 crawl.py -t "$dom" -r googleimage -p "${prxe[1]}"
  python3.8 crawl.py -t "$dom" -r bing -p "${prxe[2]}"
	# bash ts.sh "$dom" "$px"
elif [ "$go" == "p" ]; then
	cou=1
	for prx in "${prxe[@]}"
	do
		idx=$(($cou % $tref))
		# echo "$cou. $prx"
		echo "$cou. python3.8 crawl.py -t $dom -r ${refe[$idx]} -p $prx"
		# python3.8 crawl.py -t "$dom" -r "${refe[$cou]}" -p "$prx"
		
		dly=$(shuf -i 3-10 -n 1)
		# echo "$dly"
		# sleep 3
		((cou++))
	done

else
	echo "Set par 2!"
	# echo "$go"
	exit 0
fi

echo ""
echo -e " == [\e[32mRunning\e[0m] == "
echo ""
