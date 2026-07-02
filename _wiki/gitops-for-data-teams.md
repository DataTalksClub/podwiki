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
---

GitOps for data teams means moving operational data-platform changes through
Git so another person can review them before automation applies them. The
changed object might be a cloud resource, an IAM permission, a deployment
template, or a repository standard. GitOps sits inside
[DataOps]({{ '/wiki/dataops/' | relative_url }}). It overlaps with
[CI/CD]({{ '/wiki/ci-cd/' | relative_url }}),
[data governance]({{ '/wiki/data-governance/' | relative_url }}), and
[security]({{ '/wiki/security/' | relative_url }}). It also belongs near
[data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}),
[MLOps]({{ '/wiki/mlops/' | relative_url }}), and
[ML platforms]({{ '/wiki/ml-platforms/' | relative_url }}).

[Tomasz Hinc]({{ '/people/tomaszhinc/' | relative_url }}) gives the clearest
GitOps example. In
[DataOps and GitOps Best Practices for Data Teams at 12:40-26:21]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }}),
data workers open merge requests for infrastructure instead of waiting for a
platform-team ticket. [Bart Vandekerckhove]({{ '/people/bartvandekerckhove/' | relative_url }})
uses the same review model for access management in
[Data Governance and Data Access Management at 50:08-55:56]({{ '/podcasts/data-governance-data-access-management/' | relative_url }}).
[Maria Vechtomova]({{ '/people/mariavechtomova/' | relative_url }}) places Git
and CI/CD inside a standardized MLOps foundation. She also includes registries
and deployment paths in
[Pragmatic and Standardized MLOps at 16:27-18:41]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}).

## Reviewable Desired State

Guests converge on one GitOps definition: teams describe the desired state of a
data platform in code. They can review, repeat, and recover that desired state.
Git records the change. The pull request creates a review boundary, and
automation shows or applies the plan. Tomasz uses Terraform, Terragrunt, and
Atlantis for infrastructure as code
([DataOps and GitOps Best Practices for Data Teams at 23:04-26:21]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }})).

Bart applies Terraform, IAM, and pull requests to access-as-code
([Data Governance and Data Access Management at 50:08]({{ '/podcasts/data-governance-data-access-management/' | relative_url }})).
Maria adds repository standards, reusable CI/CD, and model registries. She also
adds monitoring and deployment templates
([Pragmatic and Standardized MLOps at 18:41-33:24]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})).

The guests describe guided self-service rather than unmanaged self-service. A
data scientist, analyst, or data engineer learns enough Git and cloud to
propose a useful change. They also learn enough IAM and
[CI/CD]({{ '/wiki/ci-cd/' | relative_url }}) to make the change reviewable.

Platform, SRE, security, or [DataOps]({{ '/wiki/dataops/' | relative_url }})
reviewers keep the shared platform coherent. Tomasz makes this boundary explicit
in his onboarding discussion. He describes platform teams that review merge
requests and teach safer conventions. They also support data teams during onboarding
([DataOps and GitOps Best Practices for Data Teams at 13:07 and 29:34-41:52]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }})).

## Infrastructure Changes Through Pull Requests

Tomasz gives the most concrete infrastructure path for data teams. A data worker
may need an S3 bucket, Kinesis stream, IAM role, or another cloud resource.
Instead of asking a platform engineer to create it manually, the person creates
a branch, edits Terraform or Terragrunt code, and opens a merge request.
Atlantis shows the Terraform plan before anything changes in production
([DataOps and GitOps Best Practices for Data Teams at 20:56-26:21]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }})).
The risky action becomes a diff, a plan, and a review.

Small data-platform requests often block delivery. A pipeline may need a storage
bucket, a streaming use case may need a topic or stream, and a CI job may need a
role.

GitOps gives the platform team a way to keep standards without turning every
change into a private ticket queue. It also gives analysts, data scientists, and
data engineers a safer route into platform work than running Terraform locally
with unclear credentials.

[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
describes the wider platform version of the same boundary in
[Building Production ML Platforms at 8:11-10:47]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
He names cloud infrastructure, Kubernetes, and Terraform as core platform
skills. He then argues that platform teams need to understand data-science
workflows.

GitOps covers part of that episode. The same design
constraint still appears: platform teams provide reusable paths, while product
teams avoid designing production infrastructure from scratch. GitOps therefore
sits beside [platform adoption]({{ '/wiki/platform-adoption/' | relative_url }}) and
[developer experience]({{ '/wiki/developer-experience/' | relative_url }}).

## Access as Code

Permission changes put GitOps in governance work because teams now review
access instead of buckets or deployments.

Cloud lakes and warehouses weaken old walls between systems and consumers, as
Bart describes at
[11:20 in Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }}).
As more teams reach shared data, dataset-level access management becomes a
platform responsibility.

Early access-as-code can use Terraform, CloudFormation, IAM, and pull requests.
Those tools give teams reviewability and a durable audit trail
([Data Governance and Data Access Management at 50:08-55:56]({{ '/podcasts/data-governance-data-access-management/' | relative_url }})).

Bart's warning is that code alone doesn't scale governance because teams still
need dataset ownership and request purpose. They also need approval, expiry, and
revocation. He covers purpose-based requests at 29:36, time-bound access and
revocation at 32:08, and debugging access at 35:35
([Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }})).

That makes Git the storage and review layer for permission changes, not the full
governance model. [Governance]({{ '/wiki/governance/' | relative_url }})
supplies ownership and purpose. It also supplies approval and review.
[Security]({{ '/wiki/security/' | relative_url }}) sets the risk boundary for
sensitive data, temporary debugging access, and privilege creep.

## Standardized MLOps Paths

Maria's MLOps discussion shifts GitOps from individual infrastructure changes to
standard delivery paths. She recommends using infrastructure that many
organizations already have. Her examples are Kubernetes, Git, and CI/CD. Teams
can start there before buying or building a new platform layer
([Pragmatic and Standardized MLOps at 16:27]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})).

At 18:41, she lists version control and CI/CD as foundational pieces. She also
lists registries and model registries. Deployment paths, monitoring, and
authentication belong in the same foundation.

Her standardization point is practical. Product teams often have orchestration
and CI/CD somewhere in the company, but they still struggle to use those
foundations consistently. A central MLOps team can provide repository templates
and service principals. It can also provide reusable CI/CD and monitoring so
teams don't rebuild the same delivery machinery
([Pragmatic and Standardized MLOps at 12:42 and 29:55-33:24]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})).

The same operating model appears in
[MLOps vs DataOps]({{ '/wiki/mlops-vs-dataops/' | relative_url }}).
Both disciplines use automation, review, and standard paths to make production
work less fragile.

## Reproducibility and Recovery

GitOps only helps when the code path is reproducible. Tomasz ties GitOps to
fixed dependency versions and Docker images. He also links it to GitLab CI and
production data checks in
[DataOps and GitOps Best Practices for Data Teams at 58:26-1:02:28]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }}).
He warns that a green orchestrator status isn't enough when a job inserts zero
records. The platform needs versioned code, known environments, and checks that
match real data outcomes.

[Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }}) makes the
same [DataOps]({{ '/wiki/dataops/' | relative_url }}) reliability argument in
[Mastering DataOps at 6:42 and 33:47-34:37]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}).
He frames DataOps around reducing production errors, shortening deployment
cycles, and improving team productivity. Version control and tests belong in
the same reliability system as CI/CD. Runbooks, automation, and observability
belong there too.

Maria extends the recovery story to ML delivery. Version control and reusable
CI/CD form an early maturity layer. Registries and deployment templates extend
that layer. Monitoring, traceability, and rollback do too
([Pragmatic and Standardized MLOps at 18:41-24:01]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})).

In these episodes, GitOps isn't the slogan "put everything in Git." It
combines versioned desired state and automated checks. Human review and
reproducible environments help teams understand and reverse a bad deployment or
data-platform change.

## Team Boundaries and Adoption

Tomasz doesn't describe GitOps as self-service without support. Platform, SRE,
security, and DataOps teams still guide and review changes. That support
matters when data teams first use Terraform, Terragrunt, or Atlantis. It also
matters around IAM and cloud resources
([DataOps and GitOps Best Practices for Data Teams at 13:07, 29:34, and 47:55]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }})).

Pairing and Slack support help data workers learn the path. Live coding,
templates, and documentation also reduce the need for specialist infrastructure
work on every operational task.

The adoption risk is over-standardization. If the GitOps path hides too much,
data teams return to tickets or console edits. If it leaves too much open, the
platform loses security, reproducibility, and recovery. The useful middle ground
is a paved road with clear repositories, templates, and plan output. It also has
documented approval paths and humans available when the diff isn't obvious.

Simon discusses user-centered platform design at 10:47, while Maria discusses
centralized MLOps teams at 27:06-38:01. Together, those episodes show that
balance
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})).
