---
layout: wiki
title: "GitOps for Data Teams"
summary: "How DataTalks.Club guests describe GitOps, infrastructure as code, access-as-code, and reviewable platform changes for data teams."
related:
  - DataOps
  - MLOps and DataOps
  - CI/CD
  - Governance
  - Data Governance
---

GitOps for data teams means making infrastructure, permissions, pipeline
configuration, and deployment changes through versioned code. Teams review those
changes in pull requests instead of making one-off console edits or running
laptop commands. GitOps sits inside [DataOps]({{ '/wiki/dataops/' | relative_url }})
and overlaps with [CI/CD]({{ '/wiki/ci-cd/' | relative_url }}),
[Governance]({{ '/wiki/governance/' | relative_url }}), and
[MLOps and DataOps]({{ '/wiki/mlops-and-dataops/' | relative_url }}).

Podcast guests describe GitOps as an operating model, not a tool brand. Data
scientists, analysts, and engineers can request cloud resources by changing code.
Those resources can include a bucket, role, or runner. They can also include a
deployment path or access policy. A platform, security, or governance reviewer
can check the diff.

Automation can show the planned change, and the team can recover because Git
records the desired state.

## Link Map

Use these wiki pages for the platform and governance context:

- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [MLOps and DataOps]({{ '/wiki/mlops-and-dataops/' | relative_url }})
- [CI/CD]({{ '/wiki/ci-cd/' | relative_url }})
- [Governance]({{ '/wiki/governance/' | relative_url }})
- [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
- [Security]({{ '/wiki/security/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})

Start with these podcast interviews:

- [DataOps and GitOps Best Practices for Data Teams]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }}) with [Tomasz Hinc]({{ '/people/tomaszhinc/' | relative_url }})
- [Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }}) with [Bart Vandekerckhove]({{ '/people/bartvandekerckhove/' | relative_url }})
- [Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}) with [Maria Vechtomova]({{ '/people/mariavechtomova/' | relative_url }})

## Common Definition

GitOps means moving operational changes through Git, so teams can review, repeat,
and teach those changes.

In
[DataOps and GitOps Best Practices for Data Teams]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }}),
Tomasz Hinc describes a common data-team moment. Someone needs an S3 bucket,
Kinesis stream, or IAM role. They may need another cloud resource and expect a
platform team to create it manually. Instead, the platform team sends them to the
Terraform repository and asks for a merge request. The platform team then reviews
and guides the change.

With that workflow, teams change the responsibility boundary. The platform or
security team doesn't disappear because it still reviews, teaches, and protects
production.
The data worker also doesn't become a full-time infrastructure specialist. They
learn enough Git, command line, and cloud to make their own work less blocked.

They also learn enough IAM and CI/CD, which Tomasz frames as DataOps enablement.

The platform team helps data people produce meaningful results faster and with
less fear. It doesn't do all operational work for them.

## Guest Differences

The guests differ mainly on what the team manages through code. Tomasz focuses
on infrastructure and developer enablement in
[DataOps and GitOps Best Practices for Data Teams]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }}).
His examples include Terraform, Terragrunt, Atlantis, and Docker images. He also
covers CI runners, IAM roles, and migration from Jenkins to GitLab CI.

Bart Vandekerckhove applies the same approach to access control in
[Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }}):
access requests can start in Terraform or IAM. As platforms gain more data
products and consumers, access-as-code needs ownership and approval. It also
needs review and revocation processes around it.

Maria Vechtomova, in
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}),
uses similar mechanics for ML delivery. Her examples include version control,
reusable CI/CD, registries, and deployment templates. She also covers monitoring
and emphasizes standardized repositories.
She emphasizes pragmatic standardization rather than buying a separate tool for
every MLOps category.

In her view, large organizations often already have Git and Kubernetes. They may
also have orchestration and CI/CD. Teams still struggle to use those foundations
consistently.

## Reviewable Infrastructure Changes

Tomasz gives a clear GitOps example with Terraform, Terragrunt, and Atlantis. A
person creates a branch and edits infrastructure code. They open a merge request.
Atlantis then shows what Terraform would change before anything is
applied in production
([DataOps and GitOps Best Practices for Data Teams]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }})).
The dry run turns an intimidating infrastructure action into a diff and a
planned state that other people can check.

GitOps also lowers local-machine risk. Without it, a data analyst or data
scientist might need the right Terraform version. They might also need cloud
credentials and operational confidence on their laptop. With GitOps, the change
goes through a shared repository and automation path. The person still needs to
understand what they're requesting, but the execution environment and review path
are shared.

## Access as Code

GitOps becomes governance work when the changed object is a permission rather
than a bucket or deployment. Bart explains that cloud data platforms remove the
"Chinese walls" that used to exist between source systems. Data moves into lakes
and warehouses where many consumers can reach it
([Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }})).
Bart treats dataset-level access management as a platform concern.

Early access-as-code often starts with Terraform, CloudFormation, IAM, and pull
requests. Bart's warning is that this doesn't scale alone.

As more data
products and consumers appear, the team needs purpose-based access requests and
approvals. It also needs periodic reviews and revocation. DPO, CISO, and
governance stakeholders need visibility. Data owners need visibility too.

Access-as-code gives a reviewable mechanism, and [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
provides the ownership and policy context.

## Reproducibility and Recovery

GitOps is valuable only if the code path is reproducible. Tomasz's production
examples include fixed dependency versions, Docker images, and CI migration. He
also describes a library silently changing because a requirements file didn't
pin versions
([DataOps and GitOps Best Practices for Data Teams]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }})).
He also warns that green orchestration status isn't enough: a job can be green
while inserting zero records.

Maria makes the same point for ML systems. In
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}),
she treats version control, CI/CD, and registries as early maturity foundations.
She also includes deployment paths, traceability, and rollback. GitOps isn't just
"everything in Git." It combines versioned desired state and automated checks.

It also combines review, reproducible environments, and a recovery path.

## Enablement and Team Design

Podcast guests don't frame GitOps as self-service without support. Tomasz says
platform, SRE, security, and DataOps teams should guide and review changes. That
matters most when someone first uses Terraform or Terragrunt. It also matters
when they first use Atlantis, IAM, or cloud resources
([DataOps and GitOps Best Practices for Data Teams]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }})).

Teams can provide that guidance through pairing and Slack support. They can also
use live coding, templates, and documentation.

Maria's MLOps setup follows the same model at organizational scale. A central
team provides standardized infrastructure, reusable CI/CD, and authentication.
It also provides monitoring and templates. Product teams don't have to rebuild
them separately
([Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})).

GitOps connects to [Platform Adoption]({{ '/wiki/platform-adoption/' | relative_url }})
and [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}). The paved road
must be understandable enough for data teams to use. It must also be strict
enough to keep production safe.

## Related Pages

These pages cover adjacent platform, governance, and delivery topics:

- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [MLOps and DataOps]({{ '/wiki/mlops-and-dataops/' | relative_url }})
- [CI/CD]({{ '/wiki/ci-cd/' | relative_url }})
- [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
- [Security]({{ '/wiki/security/' | relative_url }})
