---
layout: wiki
title: "GitOps for Data Teams"
summary: "How DataTalks.Club guests describe GitOps, infrastructure as code, access-as-code, and reviewable platform changes for data teams."
related:
  - DataOps
  - MLOps
  - CI/CD
  - Governance
  - Data Governance
  - Security
  - Data Engineering Platforms
  - LLMOps
  - MLOps vs DevOps
---

GitOps for data teams means moving operational data-platform changes through
Git so another person can review them before automation applies them. The
changed object may be a cloud resource or an IAM permission. It may also be a
deployment template or repository standard.

In DataTalks.Club episodes, GitOps sits inside [[DataOps]] and overlaps with
[[ci-cd=>CI/CD]] and
[[data governance]]. It also overlaps with [[security]],
[[data engineering platforms]], [[MLOps]], and [[ML platforms]].

The clearest data-team example is infrastructure as code. A data worker opens a
merge request for a cloud resource. Atlantis shows the Terraform plan. The
platform team reviews the change before it reaches production[[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps and GitOps Best Practices for Data Teams]].

The same review model appears in access management when teams manage IAM and
dataset access with Terraform-style workflows[[cite:data-governance-data-access-management=>Data Governance and Data Access Management]].
MLOps standardization adds Git and reusable CI/CD to the same operating model.
Registries and deployment paths belong there too[[cite:pragmatic-and-standardized-mlops=>Pragmatic and Standardized MLOps]].

## Reviewable Desired State

Data teams use GitOps to describe the desired state of a data platform in code.
Teams review the change in Git. Automation then plans or applies it.
Terraform, Terragrunt, and Atlantis make the desired state reviewable for
infrastructure changes[[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps and GitOps Best Practices for Data Teams]].

Terraform and CloudFormation can manage access changes. IAM and pull requests
make those changes reviewable[[cite:data-governance-data-access-management=>Data Governance and Data Access Management]].

Repository standards and reusable CI/CD extend it into [[MLOps]]. Model
registries, monitoring, and deployment templates support the same path[[cite:pragmatic-and-standardized-mlops=>Pragmatic and Standardized MLOps]].

This is guided self-service rather than unmanaged self-service. A data
scientist, analyst, or data engineer learns enough Git and cloud to propose a
useful change. IAM and [[ci-cd=>CI/CD]] skills make the change reviewable.
Platform reviewers keep the shared platform coherent. SRE, security, and
[[DataOps]] reviewers also teach conventions and support onboarding[[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps and GitOps Best Practices for Data Teams]].

## Boundaries Across Domains

The episodes don't disagree on whether Git should record operational changes.
The boundary differs by domain. Infrastructure GitOps treats the pull request
as the control point for resources such as S3 buckets and Kinesis streams. IAM
roles and other cloud objects follow the same route[[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps and GitOps Best Practices for Data Teams]].

Access governance treats Git as one layer in a broader model that still needs
dataset ownership and request purpose. It also needs approval, expiry,
revocation, and debugging access[[cite:data-governance-data-access-management=>Data Governance and Data Access Management]].
MLOps standardization treats Git and CI/CD as part of a larger delivery
foundation. Registries, monitoring, authentication, and deployment templates
round out that foundation[[cite:pragmatic-and-standardized-mlops=>Pragmatic and Standardized MLOps]].

Production ML platform work emphasizes cloud infrastructure, Kubernetes,
Terraform, and user-centered platform design. Platform teams provide reusable
paths. Product teams avoid designing production infrastructure from scratch[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]].
GitOps covers the reviewable-change part of that platform model. It belongs
beside [[platform adoption]] and [[developer experience]] rather than replacing
them.

## Infrastructure Changes Through Pull Requests

Infrastructure work starts with a small platform need. A data worker may need
an S3 bucket or IAM role. Streaming work may need a Kinesis stream or another
cloud resource.

Instead of asking a platform engineer to create it manually, the person creates
a branch and edits Terraform or Terragrunt code. Then they open a merge request.
Atlantis shows the Terraform plan before anything changes in
production[[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps and GitOps Best Practices for Data Teams]].
The risky action becomes a diff, a plan, and a review before production.

Small data-platform requests often block delivery. A pipeline may need a
storage bucket, while a streaming use case may need a topic or stream. A CI job
may need a role. GitOps lets the platform team keep standards without turning
every change into a private ticket queue. It also gives analysts, data
scientists, and data engineers a safer route into platform work than running
Terraform locally with unclear credentials.

## Access as Code

Permission changes put GitOps inside governance work because teams review
access instead of buckets or deployments. Cloud lakes and warehouses weaken old
walls between systems and consumers. As more teams reach shared data,
dataset-level access management becomes platform work[[cite:data-governance-data-access-management=>Data Governance and Data Access Management]].

Access-as-code can begin with Terraform, CloudFormation and IAM. Pull requests
give teams reviewability and a durable audit trail[[cite:data-governance-data-access-management=>Data Governance and Data Access Management]].
Code alone doesn't scale governance because teams still need dataset ownership
and request purpose. They also need approval, expiry, revocation, and debugging
access[[cite:data-governance-data-access-management=>Data Governance and Data Access Management]].

Git is the storage and review layer for permission changes, not the full
governance model. [[Governance]] supplies ownership, purpose, approval, and
review. [[Security]] sets the risk boundary for sensitive data, temporary
debugging access, and privilege creep.

## Standardized MLOps Paths

MLOps shifts GitOps from individual infrastructure changes to standard delivery
paths. Teams can start with Git and CI/CD because many organizations already
have those tools. Kubernetes may already be available too[[cite:pragmatic-and-standardized-mlops=>Pragmatic and Standardized MLOps]].

Version control and CI/CD form the foundation alongside registries and model
registries. Deployment paths, monitoring, and authentication belong there
too[[cite:pragmatic-and-standardized-mlops=>Pragmatic and Standardized MLOps]].

Standardization matters when product teams already have orchestration and CI/CD
somewhere in the company but still struggle to use those foundations
consistently. A central MLOps team can provide repository templates, service
principals, reusable CI/CD, and monitoring. That support keeps teams from
rebuilding the same delivery machinery[[cite:pragmatic-and-standardized-mlops=>Pragmatic and Standardized MLOps]].
This connects GitOps to [[MLOps vs DataOps]]. Both disciplines use automation,
review, and standard paths to make production work less fragile.

## Reproducibility and Recovery

GitOps only helps when the code path is reproducible. Teams pin dependency
versions and Docker images while GitLab CI runs production data checks[[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps and GitOps Best Practices for Data Teams]].
A green orchestrator status isn't enough when a job inserts zero records. The
platform needs versioned code, known environments, and checks that match real
data outcomes[[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps and GitOps Best Practices for Data Teams]].

The same [[DataOps]] reliability argument appears in discussions of production
error reduction, shorter deployment cycles, and team productivity. Version
control and tests belong in the same reliability system as CI/CD. Runbooks,
automation, and observability belong there too[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]].
ML delivery extends that recovery story with registries and deployment
templates. Monitoring, traceability, and rollback support the same recovery
path[[cite:pragmatic-and-standardized-mlops=>Pragmatic and Standardized MLOps]].

GitOps is therefore more than "put everything in Git." It combines versioned
desired state, automated checks, human review and reproducible environments so
teams can understand and reverse a bad deployment or data-platform change.

## Team Boundaries and Adoption

GitOps isn't self-service without support. Platform teams, DataOps, SRE and
security still guide and review changes. That support matters when data teams
first use Terraform or Terragrunt. It also matters around Atlantis, IAM and
cloud resources[[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps and GitOps Best Practices for Data Teams]].

Pairing and Slack support help data workers learn the path. Live coding,
templates, and documentation reduce the need for specialist infrastructure work
on every operational task.

Teams need enough standardization to protect the platform without hiding the
change path. If the GitOps path hides too much, data teams return to tickets or
console edits. If it leaves too much open, the platform loses security,
reproducibility, and recovery.

Useful paved roads include clear repositories and templates. Plan output,
documented approval paths, and humans help when the
diff isn't obvious[[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps and GitOps Best Practices for Data Teams]].
Production ML platform discussions show the same balance through
user-centered platform design and centralized MLOps support[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]][[cite:pragmatic-and-standardized-mlops=>Pragmatic and Standardized MLOps]].

## Related Pages

These pages connect GitOps to the operating practices around it.

- [[DataOps]]
- [[MLOps]]
- [[MLOps vs DataOps]]
- [[ci-cd=>CI/CD]]
- [[data governance]]
- [[security]]
- [[platform adoption]]
- [[developer experience]]
