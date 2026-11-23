
# Michael Evans - Assignment 7

def dissect_packet(src_ip, dst_ip, protocol, payload_bytes, flags=None):
    # Build and return the packet dictionary
    packet = {
        "src": src_ip,
        "dst": dst_ip,
        "proto": protocol.upper(),
        "length": payload_bytes if payload_bytes >= 0 else 0,
        "syn_flag": False
    }

    if flags and "SYN" in flags:
        packet["syn_flag"] = True

    return packet
