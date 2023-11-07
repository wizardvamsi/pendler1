api_key

base_fare = 110  # base fare
tim_fare_permin = 0.4  # time fare per min
Drop_dist = 18.4  # drop distance
Drop_tim = 34.9  # drop time
ref_perc = 2  # referral percentage
tim_fare = float(Drop_tim)*float(tim_fare_permin)
DF1_per = 1  # distance fare bw 0 and 2 kms
DF2_per = 5  # distance fare bw 2 and 4 kms
DF3_per = 30  # distance fare bw 4 and 6 kms
DF4_per = 15  # distance fare bw 6 and 10 kms
DF5_per = 18  # distance fare bw 10 and 200 kms
Tax_GST_perc = 5  # GST percentage
peak_tperc = 25  # peak time percentage charges
peak_time = True  # peak time
lpf_per = 1  # late pickup fare per minute
delay_time = 130
pickup_dist = 4  # pickup distance
pck_crg_permin = 10  # pickup charges per
pck_limit_cap = 3

cancel = True
# minimum distance driver should travel for cancellation fee to apply in kms
min_dist_cncl = 1.8
min_time_cncl = 3  # minimum time duration in which cancellation fee is applied in mins
cncl_fee_perkm = 15
cncl_fee_permin = 20
cncl_dist = 3
cncl_time = 5
