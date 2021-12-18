import math


def main():
    print("First test: ", first(get_test_input()))
    print("First real: ", first(get_input()))
    print("Second test: ", second(get_test_input()))
    print("Second real: ", second(get_input()))


def first(inputs: str):
    b = bin(int(inputs, 16))[2:].zfill(len(inputs) * 4)
    a, vrs = handle_packet(b)
    return sum(vrs)


def second(inputs: str):
    b = bin(int(inputs, 16))[2:].zfill(len(inputs) * 4)
    a, r = calculate_packet(b)
    return r


def calculate_packet(packet: str):
    _ = [int(packet[:3], 2)]
    idd = int(packet[3:6], 2)
    packets = []
    if idd == 4:
        return get_value(packet[6:])
    elif packet[6] == '0':
        length = int("".join(packet[7:22]), 2)
        a = packet[22:]
        while len(a) > len(packet[22 + length:]):
            a, p = calculate_packet(a)
            packets.append(p)
        return a, calculate_packets(packets, idd)
    else:
        length = int("".join(packet[7:18]), 2)
        a = packet[18:]
        for i in range(length):
            a, p = calculate_packet(a)
            packets.append(p)
        return a, calculate_packets(packets, idd)


def calculate_packets(packets, idd):
    if idd == 0:
        return sum(packets)
    if idd == 1:
        return math.prod(packets)
    if idd == 2:
        return min(packets)
    if idd == 3:
        return max(packets)
    if idd == 5:
        return 1 if packets[0] > packets[1] else 0
    if idd == 6:
        return 1 if packets[0] < packets[1] else 0
    if idd == 7:
        return 1 if packets[0] == packets[1] else 0


def handle_packet(packet: str):
    vrs = [int(packet[:3], 2)]
    idd = int(packet[3:6], 2)
    if idd == 4:
        a, b = get_lit(packet[6:])
    elif packet[6] == '0':
        length = int("".join(packet[7:22]), 2)
        a = packet[22:]
        while len(a) > len(packet[22 + length:]):
            a, v = handle_packet(a)
            vrs += v
    else:
        length = int("".join(packet[7:18]), 2)
        a = packet[18:]
        for i in range(length):
            a, v = handle_packet(a)
            vrs += v
    return a, vrs


def get_lit(a: str):
    b = []
    while a[0] != '0':
        b += a[1:5]
        a = a[5:]
    b += a[1:5]
    a = a[5:]
    return a, b


def get_value(a: str):
    a, b = get_lit(a)
    return a, int("".join(b), 2)


def get_test_input():
    return "38006F45291200"


def get_input():
    return "020D74FCE27E600A78020200DC298F1070401C8EF1F21A4D6394F9F48F4C1C00E3003500C74602F0080B1720298C400B7002540095003DC00F601B98806351003D004F66011148039450025C00B2007024717AFB5FBC11A7E73AF60F660094E5793A4E811C0123CECED79104ECED791380069D2522B96A53A81286B18263F75A300526246F60094A6651429ADB3B0068937BCF31A009ADB4C289C9C66526014CB33CB81CB3649B849911803B2EB1327F3CFC60094B01CBB4B80351E66E26B2DD0530070401C82D182080803D1C627C330004320C43789C40192D002F93566A9AFE5967372B378001F525DDDCF0C010A00D440010E84D10A2D0803D1761045C9EA9D9802FE00ACF1448844E9C30078723101912594FEE9C9A548D57A5B8B04012F6002092845284D3301A8951C8C008973D30046136001B705A79BD400B9ECCFD30E3004E62BD56B004E465D911C8CBB2258B06009D802C00087C628C71C4001088C113E27C6B10064C01E86F042181002131EE26C5D20043E34C798246009E80293F9E530052A4910A7E87240195CC7C6340129A967EF9352CFDF0802059210972C977094281007664E206CD57292201349AA4943554D91C9CCBADB80232C6927DE5E92D7A10463005A4657D4597002BC9AF51A24A54B7B33A73E2CE005CBFB3B4A30052801F69DB4B08F3B6961024AD4B43E6B319AA020020F15E4B46E40282CCDBF8CA56802600084C788CB088401A8911C20ECC436C2401CED0048325CC7A7F8CAA912AC72B7024007F24B1F789C0F9EC8810090D801AB8803D11E34C3B00043E27C6989B2C52A01348E24B53531291C4FF4884C9C2C10401B8C9D2D875A0072E6FB75E92AC205CA0154CE7398FB0053DAC3F43295519C9AE080250E657410600BC9EAD9CA56001BF3CEF07A5194C013E00542462332DA4295680"


if __name__ == '__main__':
    main()
