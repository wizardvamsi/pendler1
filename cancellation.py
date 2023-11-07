import creds
cancel = creds.cancel
min_dist_cncl = creds.min_dist_cncl
min_time_cncl = creds.min_time_cncl
cncl_fee_perkm = creds.cncl_fee_perkm
cncl_fee_permin = creds.cncl_fee_permin
cncl_dist = creds.cncl_dist
cncl_time = creds.cncl_time


if cancel == True:
    if float(cncl_dist) > float(min_dist_cncl):
        canc_fee1 = float(cncl_dist)*float(cncl_fee_perkm)
    if float(cncl_time) > float(min_time_cncl):
        canc_fee2 = (float(cncl_time)-float(min_time_cncl)) * \
            float(cncl_fee_permin)

if canc_fee1 > canc_fee2:
    canc_fee = canc_fee1
else:
    canc_fee = canc_fee2

if canc_fee > 40:
    canc_fee = 40

print("can1 :" + str(canc_fee1))
print("can2 :" + str(canc_fee2))
print("Cancellation Fee :" + str(canc_fee))
