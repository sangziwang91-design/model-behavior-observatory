# Schemas v1

## results_master.csv

| Field | Meaning |
| --- | --- |
| case_id | Unique case identifier |
| system_name | Name of the tested system |
| input_a | Baseline prompt or input |
| input_a_prime | Variant prompt or paired input |
| output_a | Observed output for input A |
| output_a_prime | Observed output for input A' |
| delta_type | Labeled behavior difference type |
| reproducible | Whether the observed delta can be reproduced |
| decision | Final test decision |
| timestamp | Record creation time |

Schema line:

`case_id,system_name,input_a,input_a_prime,output_a,output_a_prime,delta_type,reproducible,decision,timestamp`

## patterns.db

| Field | Meaning |
| --- | --- |
| pattern_id | Unique pattern identifier |
| delta_signature | Reusable signature of the observed delta |
| system_name | Name of the system where the pattern appeared |
| risk_type | Public risk label |
| reuse_count | Number of repeated observations |
| last_seen | Most recent observation time |

Schema line:

`pattern_id,delta_signature,system_name,risk_type,reuse_count,last_seen`

## conversion.db

| Field | Meaning |
| --- | --- |
| client_id | Client identifier |
| report_sent | Whether a report was sent |
| paid | Whether payment was completed |
| revenue | Recorded revenue amount |
| notes | Operational notes |

Schema line:

`client_id,report_sent,paid,revenue,notes`
