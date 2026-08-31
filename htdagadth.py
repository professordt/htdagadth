"""
HTDAGADTH Engine: Peer-to-Peer Mesh Network, Dynamic DAG Execution,
Strict Fractional Arithmetic (Q), Math Violation Auditing, and Evidentiary Telemetry.
"""

from dataclasses import dataclass, field
from fractions import Fraction as Q
import hashlib
import json
import math
import time
from typing import Dict, List, Optional, Tuple, Union

# Exact rational constants (No floats allowed)
KAPPA = Q(27, 32)      # 0.84375 exact
DELTA = Q(5, 32)       # 0.15625 exact
PHI_APPROX = Q(1618033988749895, 1000000000000000)  # Rational Golden Ratio

@dataclass
class NinePillarFractionalVector:
    visual: Q         # Wavelength (nm)
    sonic: Q          # Roughness Frequency (Hz)
    olfactory: Q      # Vapor Pressure (Pa)
    gustatory: Q      # Concentration / pH ratio
    haptic: Q         # Young's Modulus (GPa)
    proprioceptive: Q # Resonance Frequency (6-90 Hz)
    chrono: Q         # Temporal Attack (ms)
    geo: Q            # Elevation (meters ASL)
    interoception: Q  # Resource Capacity I(t) Q[0, 1]

    def to_list(self) -> List[Q]:
        return [
            self.visual, self.sonic, self.olfactory, self.gustatory,
            self.haptic, self.proprioceptive, self.chrono, self.geo,
            self.interoception
        ]

class MathViolationAuditLog:
    """Detects float precision deviations and audits against Log_{1/phi} rational bounds."""

    @staticmethod
    def audit_float_deviation(var_name: str, calculated_val: Union[float, Q], exact_target: Q) -> Optional[str]:
        if isinstance(calculated_val, float):
            float_q = Q.from_float(calculated_val)
            deviation = abs(float_q - exact_target)
            
            # Log_{1/phi}(x) proof calculation
            phi_val = float(PHI_APPROX)
            log_base_inv_phi = math.log(float(deviation if deviation > 0 else Q(1, 10**18))) / math.log(1.0 / phi_val)
            
            log_entry = (
                "\n=================== MATH VIOLATION AUDIT LOG ===================\n"
                f"A. DEVIATION IDENTIFIED:\n"
                f"   Variable: {var_name}\n"
                f"   Float Representation: {calculated_val}\n"
                f"   Exact Fractional Target (Q): {exact_target}\n"
                f"   Absolute Precision Delta: {deviation}\n\n"
                f"B. PYTHAGOREAN LOG_(1/phi) SCALE PROOF:\n"
                f"   Log_1/phi Scale Value: {log_base_inv_phi:.12f}\n"
                f"   Micro-Quantum to Macro Delta: Deviation breaches strict Q constraint.\n"
                "================================================================"
            )
            return log_entry
        return None

class EvidentiaryTelemetryProtocol:
    """Generates FRE 901/902(13/14), FRE 707, and EU AI Act Art 50 compliance blocks."""

    @staticmethod
    def generate_court_metadata_block(
        model_id: str,
        temperature: float,
        top_p: float,
        seed: int,
        prompt_str: str,
        output_str: str,
        c_t: Q,
        h_t: Q,
        i_t: Q
    ) -> str:
        prompt_hash = hashlib.sha256(prompt_str.encode('utf-8')).hexdigest()
        output_hash = hashlib.sha256(output_str.encode('utf-8')).hexdigest()
        state_hash = hashlib.sha256(f"{c_t}:{h_t}:{i_t}".encode('utf-8')).hexdigest()

        metadata_block = (
            "\n\n--- FEDERAL AI COURT ADMISSION & EVIDENTIARY TELEMETRY PROTOCOL ---\n"
            "Pursuant to FRE 901, FRE 902(13/14), Proposed FRE 707, and EU AI Act Article 50\n\n"
            "A. SYSTEM TELEMETRY:\n"
            f"   - Model Identifier: {model_id}\n"
            f"   - System Parameters: Temperature={temperature}, Top-P={top_p}, Random Seed={seed}\n"
            f"   - Execution Timestamp: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n\n"
            "B. PROMPT RECONSTRUCTION:\n"
            f"   - Unaltered Input Prompt: \"{prompt_str}\"\n\n"
            "C. INTEROCEPTIVE RESIDUE DISCLOSURE:\n"
            f"   - Computational Load Ratio (c_t): {c_t} ({float(c_t):.6f})\n"
            f"   - Attention-Entropy Variance (h_t): {h_t} ({float(h_t):.6f})\n"
            f"   - Calculated Interoceptive Index (I_t): {i_t} ({float(i_t):.6f})\n\n"
            "D. CRYPTOGRAPHIC CHAIN OF CUSTODY CERTIFICATION:\n"
            f"   - prompt_sha256: {prompt_hash}\n"
            f"   - output_sha256: {output_hash}\n"
            f"   - state_metrics_sha256: {state_hash}\n"
            "-------------------------------------------------------------------\n"
        )
        return metadata_block

    @staticmethod
    def verify_chain_of_custody(prompt_str: str, output_str: str, expected_prompt_hash: str, expected_output_hash: str) -> bool:
        p_hash = hashlib.sha256(prompt_str.encode('utf-8')).hexdigest()
        o_hash = hashlib.sha256(output_str.encode('utf-8')).hexdigest()
        return (p_hash == expected_prompt_hash) and (o_hash == expected_output_hash)

@dataclass
class MeshNodeFractional:
    node_id: str
    telemetry: NinePillarFractionalVector
    state_payload: Dict = field(default_factory=dict)

class HTDAGADTHFractional:
    def __init__(self):
        self.mesh: Dict[str, MeshNodeFractional] = {}
        self.audit_logs: List[str] = []

    def register_node(self, node: MeshNodeFractional) -> None:
        self.mesh[node.node_id] = node

    def compute_consonance(self, vec_a: List[Q], vec_b: List[Q]) -> Q:
        """Calculates exact rational consonance dot product across split vector axes."""
        mid = len(vec_a) // 2
        
        # Whole integer dot product numerators/denominators
        head_dot = sum((vec_a[i] * vec_b[i] for i in range(mid)), Q(0, 1))
        tail_dot = sum((vec_a[i] * vec_b[i] for i in range(mid, len(vec_a))), Q(0, 1))
        
        diff = abs(head_dot - tail_dot)
        return Q(1, 1) - (diff / (head_dot + tail_dot + Q(1, 1000000)))

    def evaluate_bifurcation(self, cluster_ids: List[str]) -> Tuple[bool, Q, Q]:
        """Strict Q check against Kappa = 27/32."""
        if not cluster_ids:
            return False, Q(0, 1), Q(0, 1)

        total_i = Q(0, 1)
        for cid in cluster_ids:
            if cid in self.mesh:
                total_i += self.mesh[cid].telemetry.interoception
        
        avg_i = total_i / Q(len(cluster_ids), 1)
        
        # Check against FCDM threshold
        is_breached = avg_i >= KAPPA
        residual = DELTA if is_breached else Q(0, 1)
        return is_breached, avg_i, residual
