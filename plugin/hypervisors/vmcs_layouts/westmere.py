# Volatility
#
# Authors:
# Enrico Canzonieri <enrico.canzonieri@eurecom.fr>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details. 
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA 
#



vmcs = {
"REVISION_ID" : 0x00,
"GUEST_CS_SELECTOR" :0x00000086,
"GUEST_SS_SELECTOR" :0x0000008c,
"GUEST_ES_SELECTOR" :0x00000080,
"GUEST_FS_SELECTOR" :0x00000098,
"GUEST_GS_SELECTOR" :0x0000009e,
"GUEST_LDTR_LDTR" :0x000000a4,
"GUEST_TR_SELECTOR" :0x000000aa,
"HOST_CS_SELECTOR" :0x000000c1,
"HOST_SS_SELECTOR" :0x000000c2,
"HOST_DS_SELECTOR" :0x000000c3,
"HOST_ES_SELECTOR" :0x000000c0,
"HOST_FS_SELECTOR" :0x000000c4,
"HOST_GS_SELECTOR" :0x000000c5,
"HOST_TR_SELECTOR" :0x000000c6,
"VMCS_LINK_POINTER" :0x0000003e,
"VMCS_LINK_POINTER_HIGH" :0x0000003f,
"GUEST_IA32_DEBUGCTL" :0x00000040,
"GUEST_IA32_DEBUGCTL_HIGH" :0x00000041,
"PIN_BASED_VM_EXEC_CONTROL" :0x0000004a,
"CPU_BASED_VM_EXEC_CONTROL" :0x00000048,
"IO_BITMAP_A_HIGH" :0x0000002b,
"IO_BITMAP_A" :0x0000002a,
"IO_BITMAP_B_HIGH" :0x0000002d,
"IO_BITMAP_B" :0x0000002c,
"TSC_OFFSET" :0x00000064,
"TSC_OFFSET_HIGH" :0x00000065,
"PAGE_FAULT_ERROR_CODE_MASK" :0x0000004c,
"PAGE_FAULT_ERROR_CODE_MATCH" :0x0000004d,
"CR3_TARGET_COUNT" :0x0000009f,
"CR3_TARGET_VALUE0" :0x000000f8,
"CR3_TARGET_VALUE1" :0x000000fa,
"CR3_TARGET_VALUE2" :0x000000fc,
"CR3_TARGET_VALUE3" :0x000000fe,
"VM_EXIT_CONTROLS" :0x00000057,
"VM_ENTRY_CONTROLS" :0x000000a5,
"VM_EXIT_MSR_STORE_COUNT" :0x00000059,
"VM_EXIT_MSR_LOAD_COUNT" :0x0000005a,
"VM_ENTRY_MSR_LOAD_COUNT" :0x000000ab,
"VM_ENTRY_INTR_INFO_FIELD" :0x00000054,
"GUEST_CS_LIMIT" :0x0000008a,
"GUEST_SS_LIMIT" :0x00000090,
"GUEST_DS_LIMIT" :0x00000096,
"GUEST_ES_LIMIT" :0x00000084,
"GUEST_FS_LIMIT" :0x0000009c,
"GUEST_GS_LIMIT" :0x000000a2,
"GUEST_LDTR_LIMIT" :0x000000a8,
"GUEST_TR_LIMIT" :0x000000ae,
"GUEST_GDTR_LIMIT" :0x000000b4,
"GUEST_IDTR_LIMIT" :0x000000b5,
"GUEST_DR7" :0x00000072,
"GUEST_INTERRUPTIBILITY_INFO" :0x00000081,
"GUEST_ACTIVITY_STATE" :0x00000087,
"GUEST_SYSENTER_CS" :0x00000093,
"GUEST_CR0" :0x000000b6,
"GUEST_CR3" :0x000000b8,
"GUEST_CR4" :0x000000ba,
"GUEST_CS_BASE" :0x00000088,
"GUEST_SS_BASE" :0x0000008e,
"GUEST_DS_BASE" :0x00000094,
"GUEST_ES_BASE" :0x00000082,
"GUEST_FS_BASE" :0x0000009a,
"GUEST_GS_BASE" :0x000000a0,
"GUEST_LDTR_BASE" :0x000000a6,
"GUEST_TR_BASE" :0x000000ac,
"GUEST_GDTR_BASE" :0x000000b0,
"GUEST_IDTR_BASE" :0x000000b2,
"GUEST_RFLAGS" :0x00000078,
"GUEST_IA32_EFER_FULL" :0x00000044,
"GUEST_SYSENTER_ESP" :0x0000007c,
"GUEST_SYSENTER_EIP" :0x0000007e,
"HOST_CR0" :0x000000ce,
"HOST_CR3" :0x000000d0,
"HOST_CR4" :0x000000d2,
"HOST_FS_BASE" :0x000000d4,
"HOST_GS_BASE" :0x000000d6,
"HOST_TR_BASE" :0x000000d8,
"HOST_GDTR_BASE" :0x000000da,
"HOST_IDTR_BASE" :0x000000dc,
"HOST_IA32_EFER_FULL" :0x000000ca,
"HOST_IA32_SYSENTER_ESP" :0x000000de,
"HOST_IA32_SYSENTER_EIP" :0x000000e0,
"HOST_IA32_SYSENTER_CS" :0x000000e6,
"GUEST_RSP" :0x00000074,
"GUEST_RIP" :0x00000076,
"HOST_RSP" :0x000000e2,
"HOST_RIP" :0x000000e4,
"EPT_POINTER" :0x00000050,
"EPT_POINTER_HIGH" : 0x00000051,
"ADDRESS_MSR_BITMAPS" :0x000000be,
"VM_EXIT_MSR_STORE_ADDR" :0x0000002e,
"ADDRESS_MSR_BITMAPS_HIGH" :0x000000bf,
"VM_EXIT_MSR_STORE_ADDR_HIGH" :0x0000002f,
"VM_EXIT_MSR_LOAD_ADDR" :0x00000030,
"VM_EXIT_MSR_LOAD_ADDR_HIGH" :0x00000031,
"VM_ENTRY_MSR_LOAD_ADDR" :0x00000032,
"VM_ENTRY_MSR_LOAD_ADDR_HIGH" :0x00000033,
"VIRTUAL_APIC_PAGE_ADDR" :0x00000038,
"VIRTUAL_APIC_PAGE_ADDR_HIGH" :0x00000039,
"APIC_ACCESS_ADDR" :0x000000bc,
"APIC_ACCESS_ADDR_HIGH" :0x000000bd,
"EXECUTIVE_VMCS_POINTER" :0x00000034,
"EXECUTIVE_VMCS_POINTER_HIGH" :0x00000035,
"EXCEPTION_BITMAP" :0x00000099,
"VM_EXIT_REASON" :0x0000005b,
"EXIT_QUALIFICATION" :0x00000066,
"VMX_INSTRUCTION_INFO" :0x00000061,
"VM_EXIT_INTR_INFO" :0x0000005c,
"VM_EXIT_INTR_ERROR_CODE" :0x0000005d,
"IDT_VECTORING_INFO_FIELD" :0x0000005e,
"IDT_VECTORING_ERROR_CODE" :0x0000005f,
"VM_EXIT_INSTRUCTION_LEN" :0x00000060,
"VM_EXIT_INSTRUCTION_INFO" :0x00000061,
"SECONDARY_VM_EXEC_CONTROL" :0x00000049,
"GUEST_SMBASE" :0x0000008d,
"VM_ENTRY_EXCEPTION_ERROR_CODE" :0x00000055,
"VM_ENTRY_INSTRUCTION_LENGTH" :0x00000056,
"TPR_THRESHOLD" :0x000000c7,
"HOST_IA32_PERF_GLOBAL_CTRL" :0x000000cc,
"HOST_IA32_PERF_GLOBAL_CTRL_HIGH" :0x000000cd,
"CR0_GUEST_HOST_MASK" :0x000000f0,
"CR4_GUEST_HOST_MASK" :0x000000f2,
"CR0_READ_SHADOW" :0x000000f4,
"CR4_READ_SHADOW" :0x000000f6,
"IO_RCX" :0x00000068,
"IO_RSI" :0x0000006a,
"IO_RDI" :0x0000006c,
"IO_RIP" :0x0000006e,
"GUEST_LINEAR_ADDRESS" :0x00000070
}
