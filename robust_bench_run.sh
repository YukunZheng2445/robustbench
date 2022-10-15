export OMP_NUM_THREADS=1

#
for i in 0 1 2 3 4 5
    do
        python ww_evaluate.py --attack-type corruptions --index ${i} &
    done

for i in 0 1 2 3
    do
        python ww_evaluate.py --attack-type Linf --index ${i} &
    done