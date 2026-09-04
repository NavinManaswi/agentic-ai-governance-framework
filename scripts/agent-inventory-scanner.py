#!/usr/bin/env python3
"""
Agentic AI Inventory Scanner

This script discovers and inventories AI agents in the environment.
"""

import os
import json
import subprocess
from datetime import datetime
from pathlib import Path

class AgentInventoryScanner:
    """Scans for AI agents and generates an inventory."""
    
    def __init__(self, output_dir="inventory"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.agents = []
    
    def scan_kubernetes(self):
        """Scan Kubernetes for agent deployments."""
        try:
            result = subprocess.run(
                ["kubectl", "get", "deployments", "-o", "json"],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                data = json.loads(result.stdout)
                for item in data.get("items", []):
                    name = item.get("metadata", {}).get("name", "")
                    if "agent" in name.lower():
                        self.agents.append({
                            "name": name,
                            "type": "kubernetes_deployment",
                            "namespace": item.get("metadata", {}).get("namespace", "default"),
                            "replicas": item.get("spec", {}).get("replicas", 0),
                            "discovered": datetime.now().isoformat()
                        })
        except Exception as e:
            print(f"⚠️  Kubernetes scan failed: {e}")
    
    def scan_azure(self):
        """Scan Azure for agent resources."""
        try:
            result = subprocess.run(
                ["az", "resource", "list", "--query", "[?contains(name, 'agent')]", 
                 "--output", "json"],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                data = json.loads(result.stdout)
                for item in data:
                    self.agents.append({
                        "name": item.get("name", "unknown"),
                        "type": "azure_resource",
                        "resource_group": item.get("resourceGroup", "unknown"),
                        "location": item.get("location", "unknown"),
                        "discovered": datetime.now().isoformat()
                    })
        except Exception as e:
            print(f"⚠️  Azure scan failed: {e}")
    
    def scan_aws(self):
        """Scan AWS for agent resources."""
        try:
            result = subprocess.run(
                ["aws", "resourcegroupstaggingapi", "get-resources", 
                 "--tag-filters", "Key=Type,Values=agent",
                 "--output", "json"],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                data = json.loads(result.stdout)
                for item in data.get("ResourceTagMappingList", []):
                    self.agents.append({
                        "name": item.get("ResourceARN", "unknown").split("/")[-1],
                        "type": "aws_resource",
                        "arn": item.get("ResourceARN", "unknown"),
                        "discovered": datetime.now().isoformat()
                    })
        except Exception as e:
            print(f"⚠️  AWS scan failed: {e}")
    
    def scan_github(self):
        """Scan GitHub Actions for agent workflows."""
        try:
            result = subprocess.run(
                ["gh", "workflow", "list", "--json", "name,id,state"],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                data = json.loads(result.stdout)
                for item in data:
                    if "agent" in item.get("name", "").lower():
                        self.agents.append({
                            "name": item.get("name", "unknown"),
                            "type": "github_workflow",
                            "workflow_id": item.get("id", "unknown"),
                            "state": item.get("state", "unknown"),
                            "discovered": datetime.now().isoformat()
                        })
        except Exception as e:
            print(f"⚠️  GitHub scan failed: {e}")
    
    def generate_inventory(self):
        """Generate the agent inventory report."""
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "total_agents": len(self.agents),
            "agents": self.agents,
            "summary": {
                "by_type": {}
            }
        }
        
        # Summarize by type
        for agent in self.agents:
            agent_type = agent.get("type", "unknown")
            if agent_type not in report["summary"]["by_type"]:
                report["summary"]["by_type"][agent_type] = 0
            report["summary"]["by_type"][agent_type] += 1
        
        # Write inventory
        output_file = self.output_dir / f"agent-inventory-{datetime.now().strftime('%Y%m%d')}.json"
        with open(output_file, "w") as f:
            json.dump(report, f, indent=2)
        
        print(f"✅ Inventory generated: {output_file}")
        print(f"   Total agents: {report['total_agents']}")
        print("   By type:")
        for agent_type, count in report["summary"]["by_type"].items():
            print(f"     - {agent_type}: {count}")
        
        return report

def main():
    print("🤖 Agentic AI Inventory Scanner")
    print("=" * 60)
    print("Scanning for AI agents...")
    
    scanner = AgentInventoryScanner()
    
    # Run scans
    print("\n📡 Scanning Kubernetes...")
    scanner.scan_kubernetes()
    
    print("📡 Scanning Azure...")
    scanner.scan_azure()
    
    print("📡 Scanning AWS...")
    scanner.scan_aws()
    
    print("📡 Scanning GitHub...")
    scanner.scan_github()
    
    print("\n📊 Generating inventory...")
    scanner.generate_inventory()
    
    print("\n✅ Scan complete!")

if __name__ == "__main__":
    main()
