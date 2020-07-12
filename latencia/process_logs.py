import sys

# t[1]  = 1594500696.147684
# t[2]  = 1594501134.3582737
# t[3]  = 1594501291.638637
# t[4]  = 1594501376.194533
# t[5]  = 1594501558.740212
# t[6]  = 1594501635.8626502
# t[7]  = 1594501711.0624294
# t[8]  = 1594501783.0501914
# t[9]  = 1594501871.9000678
# t[10] = 1594501970.3666008

t = {}
t[1]  = 1594559015.6399558 #0
t[2]  = 1594559108.191461  #0
t[3]  = 1594559298.9450488 #0
t[4]  = 1594559368.515848  #0

t[5]  = 1594559488.24416   #50
t[6]  = 1594559561.5366852 #50
t[7]  = 1594559625.7682614 #50
t[8]  = 1594559667.2037365 #50

t[9]  = 1594559783.7058773 #100
t[10] = 1594559836.7689416 #100
t[11] = 1594559875.3029912 #100
t[12] = 1594559920.8356504 #100

t[13] = 1594560041.713021  #150
t[14] = 1594560083.27565   #150
t[15] = 1594560124.2283773 #150
t[16] = 1594560164.1821332 #150

t[17] = 1594560312.288195  #200
t[18] = 1594560360.8180053 #200
t[19] = 1594560445.3917742 #200
t[20] = 1594560496.6397023 #200

t[21]  = 1594560638.246801  #5
t[22]  = 1594560683.9943194 #5
t[23]  = 1594560733.9712698 #5
t[24]  = 1594560778.85384   #5

t[25]  = 1594561211.170291  #10
t[26]  = 1594560963.4066916 #10
t[27]  = 1594561005.227846  #10
t[28]  = 1594561056.2586915 #10

t[29]  =  1594563472.3304653 #15
t[30]  =  1594563541.5854418 #15
t[31]  =  1594563609.6768866 #15
t[32]  =  1594563670.0629458 #15

t[33]  =  1594562636.5608106 #20
t[34]  =  1594562696.8409476 #20
t[35]  =  1594562764.088177 #20
t[36]  =  1594562810.0837498 #20

t[37]  =  1594563788.6370614 #25
t[38]  =  1594563859.7741132 #25
t[39]  =  1594563915.2417417 #25
t[40]  =  1594563958.1005664 #25

t[41]  =  1594564070.853275 #30
t[42]  =  1594564116.778249 #30
t[43]  =  1594564163.357388 #30
t[44]  =  1594564216.403998 #30

t[45]  =  1594564317.907984 #35
t[46]  =  1594564371.167436 #35
t[47]  =  1594564449.460157 #35
t[48]  =  1594564532.10944  #35

t[49]  = 1594564665.167413  #40
t[50]  = 1594564714.9399636 #40
t[51]  = 1594564772.8124905 #40
t[52]  = 1594564870.4599156 #40

t[53]  = 1594565329.7588565 #45
t[54]  = 1594565387.4684517 #45
t[55]  = 1594565440.9396    #45
t[56]  = 1594565488.8902187 #45

t[57]  = 1594565595.9491692 #50
t[58]  = 1594565647.4086    #50
t[59]  = 1594565692.0924537 #50
t[60]  = 1594565737.5349114 #50

t[61]  = 1594565881.2157297 #70
t[62]  = 1594565927.5307405 #70
t[63]  = 1594565972.7916775 #70
t[64]  = 1594566020.5517848 #70

t[65]  = 1594566102.0227618 #80
t[66]  = 1594566220.1553428 #80
t[67]  = 1594566270.568499 #80
t[68]  = 1594566316.8673306 #80

t[69]  = 1594582756.7884696 #150
t[70]  = 1594582890.6249843 #150
t[71]  = 1594582935.6994255 #150
t[72]  = 1594582984.9079256 #150

t[73]  = 1594583419.5615304 #300
t[74]  = 1594583469.0828116 #300
t[75]  = 1594583533.4295506 #300
t[76]  = 1594583596.611489 #300

t[77]  = 1594583719.7877562 #250
t[78]  = 1594583778.83989 #250
t[79]  = 1594583847.6478498 #250
t[80]  = 1594583905.150777 #250

t[81]  = 1594584048.9504714 #100
t[82]  = 1594584109.8856325 #100
t[83]  = 1594584167.3826733 #100
t[84]  = 1594584214.6355135 #100

t[85]  =  1594584683.8519945 #350
t[86]  =  1594584872.4979568 #350
t[87]  =  1594584918.6613352 #350
t[88]  =  1594584978.987718  #350

t[89]  =   1594585224.7793777 #25
t[90]  =   1594585273.3373916 #25
t[91]  =   1594585321.6198618 #25
t[92]  =   1594585376.934044 #25

latencia_array     = {}
latencia_array[1]  = 0
latencia_array[2]  = 50
latencia_array[3]  = 100
latencia_array[4]  = 150
latencia_array[5]  = 200
latencia_array[6]  = 5
latencia_array[7]  = 10
latencia_array[8]  = 15
latencia_array[9]  = 20
latencia_array[10] = 25
latencia_array[11] = 30
latencia_array[12] = 35
latencia_array[13] = 40
latencia_array[14] = 45
latencia_array[15] = 50
latencia_array[16] = 70
latencia_array[17] = 80
latencia_array[18] = 150
latencia_array[19] = 300
latencia_array[20] = 250
latencia_array[21] = 100
latencia_array[22] = 350
latencia_array[23] = 25

# t[3]  = 1594513865.1358156
# t[4]  = 1594513975.0294173
# t[5]  = 1594514586.9258096

# number of logs analized
num_logs = int(sys.argv[1])

num_logs += 1

mean_diff = 0
mean_ftt = 0

print("ms\tFTT\tDIFF")

for k in range(1,num_logs):
    filepath = "logs_80/"+str(k)+".txt"

    containers = []
    fftime = {}
    fftime[1] = 0
    fftime[2] = 0
    fftime[3] = 0
    fftime[4] = 0
    fftime[5] = 0

    diff_time = {}
    diff_time[1] = 0
    diff_time[2] = 0
    diff_time[3] = 0
    diff_time[4] = 0
    diff_time[5] = 0

    diff_number_time = {}
    diff_number_time[1] = 0
    diff_number_time[2] = 0
    diff_number_time[3] = 0
    diff_number_time[4] = 0
    diff_number_time[5] = 0

    with open(filepath) as fp:

        line = fp.readline()

        cnt = 1
        ffd_time = 0
        container_id = 0

        while line:
            # detect wich container is
            container = line.find("Container D")
            if container >= 0:
                container_id = int(line[11:12])
                containers.append(container_id)

            # detect the time frame detected
            ffd = line.find("First Frame Detected: ")
            if ffd >= 0:
                fftime[container_id] = line[22:39].replace("\r","")
                
            values = line.split(" 	 ")
            try:
                label = values[5].find("Diff Before Detection")
                if label == -1:
                    diff_time[container_id] += float(values[5])
                    diff_number_time[container_id] += 1
            except IndexError, ValueError:
                v = ''

            # print("Line {}: {}".format(cnt, line.strip()))
            line = fp.readline()
            cnt += 1

    # print(containers)
    # print(diff_time)
    # print(diff_number_time)

    for i in range(1,4):
        if diff_number_time[i] > 0:
            d = diff_time[i] / diff_number_time[i]
            dd = float(fftime[i]) - float(t[k])
            p_val = '{}\t{:.4f}\t{:.4f}'.format(i, d, dd) 
            # print(p_val.replace(".",","))

            mean_diff += d
            mean_ftt += dd

            if k%4 == 0:
                mean_diff = mean_diff / 4
                mean_ftt = mean_ftt / 4

                p_val2 = '{}\t{:.4f}\t{:.4f}'.format(latencia_array[int(k/4)], mean_ftt, mean_diff)

                print(p_val2.replace(".",","))

                mean_diff = 0
                mean_ftt = 0
