def calculate_subnet(ip_address, num_subnets, num_hosts_per_subnet):
    ip_parts = ip_address.split(".")
    network_bits = sum(bin(int(part)).count("1") for part in ip_parts)
    total_subnet_bits = network_bits + num_subnets.bit_length()

    if total_subnet_bits > 32:
        print("Error: Insufficient IP address space for the given number of subnets.")
        return

    subnet_ranges = []
    subnet_bits = network_bits

    for i in range(len(num_hosts_per_subnet)):
        subnet_hosts = (
            num_hosts_per_subnet[i] + 2
        )  # +2 for network and broadcast addresses
        subnet_range_size = 2 ** (32 - total_subnet_bits)
        subnet_ranges.append((subnet_range_size, subnet_hosts))

        if subnet_ranges[i][0] > subnet_ranges[i][1]:
            print(f"Error: Insufficient IP address space for Network {chr(65 + i)}.")
            return

        subnet_bits += subnet_ranges[i][0]
        total_subnet_bits += subnet_ranges[i][0]
        network_address = sum(
            int(part) << (24 - index * 8) for index, part in enumerate(ip_parts)
        )
        network_address &= 0xFFFFFFFF << (32 - total_subnet_bits)
        broadcast_address = network_address + subnet_ranges[i][0] - 1

        print(f"Network {chr(65 + i)}:")
        print(
            f"Subnet: {ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.{network_address >> 24}/{total_subnet_bits}"
        )
        print(
            f"Network Address: {ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.{network_address >> 24}"
        )
        print(
            f"Broadcast Address: {ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.{broadcast_address >> 24}"
        )
        print(
            f"Usable IP Range: {ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.{(network_address >> 24) + 1} - {(broadcast_address >> 24) - 1}"
        )
        print("")


# Example usage
ip_address = "200.55.1.0"
num_subnets = 6
num_hosts_per_subnet = [100, 40, 20, 10, 6, 2]

calculate_subnet(ip_address, num_subnets, num_hosts_per_subnet)
