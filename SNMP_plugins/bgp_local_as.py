#!/usr/bin/env python3
# Check plug-in for monitoring BGP Local Autonomous System Number
# OID: 1.3.6.1.2.1.15.2.0 (bgpLocalAs) from BGP4-MIB (RFC 4273)
#
# Store in your Checkmk site at:
# ~/local/lib/python3/cmk_addons/plugins/bgp/agent_based/bgp_local_as.py

from cmk.agent_based.v2 import (
    CheckPlugin,
    CheckResult,
    DiscoveryResult,
    exists,
    Result,
    Service,
    SimpleSNMPSection,
    SNMPTree,
    State,
    StringTable,
)


def parse_bgp_local_as(string_table: StringTable) -> dict | None:
    if not string_table or not string_table[0]:
        return None
    return {"bgp_local_as": string_table[0][0]}


def discover_bgp_local_as(section) -> DiscoveryResult:
    if section is not None:
        yield Service()


def check_bgp_local_as(section) -> CheckResult:
    if section is None:
        yield Result(state=State.UNKNOWN, summary="No BGP data available")
        return

    local_as = section["bgp_local_as"]
    yield Result(state=State.OK, summary=f"BGP Local AS: {local_as}")


snmp_section_bgp_local_as = SimpleSNMPSection(
    name="bgp_local_as",
    parse_function=parse_bgp_local_as,
    # Detect: only for devices that expose the BGP4-MIB (bgpLocalAs exists)
    detect=exists(".1.3.6.1.2.1.15.2.*"),
    fetch=SNMPTree(
        base=".1.3.6.1.2.1.15",
        oids=["2.0"],  # bgpLocalAs
    ),
)

check_plugin_bgp_local_as = CheckPlugin(
    name="bgp_local_as",
    sections=["bgp_local_as"],
    service_name="BGP Local AS",
    discovery_function=discover_bgp_local_as,
    check_function=check_bgp_local_as,
)
