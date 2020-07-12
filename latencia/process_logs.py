t = {}
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

t[1]  = 1594520506.3464293
t[2]  = 1594520667.0997584

# t[3]  = 1594513865.1358156
# t[4]  = 1594513975.0294173
# t[5]  = 1594514586.9258096

num_logs = 2

num_logs += 1

for k in range(1,num_logs):
    filepath = "logs/"+str(k)+".txt"

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
            p_val = '{}\t{:.4f}\t{:.4f}'.format(i, dd, d) 
            print(p_val.replace(".",","))
