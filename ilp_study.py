import m5
from m5.objects import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--width', type=int, default=1)
args = parser.parse_args()

system = System()
system.clk_domain = SrcClockDomain(clock = '1GHz', voltage_domain = VoltageDomain())
system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('512MiB')]

system.cpu = DerivO3CPU()

# ADDED THIS LINE TO FIX INTERRUPT ERROR
system.cpu.createInterruptController()

# Set widths
system.cpu.fetchWidth = args.width
system.cpu.decodeWidth = args.width
system.cpu.issueWidth = args.width
system.cpu.commitWidth = args.width

binary = 'tests/test-progs/hello/bin/x86/linux/hello'
system.workload = SEWorkload.init_compatible(binary)
process = Process(executable = binary, cmd = [binary])
system.cpu.workload = process
system.cpu.createThreads()

system.membus = SystemXBar()
system.cpu.icache_port = system.membus.cpu_side_ports
system.cpu.dcache_port = system.membus.cpu_side_ports
system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8(range=system.mem_ranges[0])
system.mem_ctrl.port = system.membus.mem_side_ports
system.system_port = system.membus.cpu_side_ports

root = Root(full_system = False, system = system)
m5.instantiate()
print("Starting simulation...")
m5.simulate()
print(f"Exiting @ tick {m5.curTick()}")
