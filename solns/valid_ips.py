def generate_ips(s):
    s = list(s)
    res = []
    ip_address = []

    def helper(num_octets, index):
        if num_octets == 4:
            if index == len(s):
                res.append('.'.join([''.join(octet) for octet in ip_address]))
            #backtrack
            return
        if len(ip_address) != 0:
            last_octet = int(''.join(ip_address[-1]))
            if last_octet == 0:
                #backtrack
                return
            if last_octet > 255:
                #backtrack
                return
        octet_sizes = [1, 2, 3]
        for size in octet_sizes:
            #create empty_octet
            ip_address.append([])
            ip_address[-1] = s[index: index + size]
            helper(num_octets + 1, index + size)
            ip_address.pop()
    
    helper(0, 0)
    return res

test = '25525511135'

print(generate_ips(test))
        

