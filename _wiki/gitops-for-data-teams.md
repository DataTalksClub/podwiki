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
  - Security
  - MLOps
  - Data Engineering Platforms
---

GitOps for data teams is the practice of moving operational data-platform
changes through Git. Cloud resources and permissions become versioned changes
that another person can review before automation applies them. Deployment paths
can follow the same route.

In the podcast archive, GitOps sits inside
[DataOps]({{ '/wiki/dataops/' | relative_url }}). It also connects to
[CI/CD]({{ '/wiki/ci-cd/' | relative_url }}),
[data governance]({{ '/wiki/data-governance/' | relative_url }}),
[security]({{ '/wiki/security/' | relative_url }}), and
[data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}).

[Tomasz Hinc]({{ '/people/tomaszhinc/' | relative_url }}) gives the clearest
archive anchor. He describes GitOps as an enablement model for data teams that
need infrastructure without a manual platform-team ticket.

[Bart Vandekerckhove]({{ '/people/bartvandekerckhove/' | relative_url }}) uses
the same operating practice in
[Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }}).
[Maria Vechtomova]({{ '/people/mariavechtomova/' | relative_url }}) applies it
to standardized MLOps in
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}).

## Common Definition

Across these episodes, GitOps means the desired state of a data platform is
reviewable, repeatable, and recoverable. The desired state may be infrastructure
as code, pipeline configuration, model-serving deployment templates, or
access-as-code. Git records the change, the pull request creates a review
boundary, and automation shows or applies the plan.

Tomasz gives the infrastructure version in
[DataOps and GitOps Best Practices for Data Teams]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }}).
A data worker may need an S3 bucket, Kinesis stream, IAM role, or another cloud
resource. Instead of asking the platform team to create it manually, the person
opens a merge request in the Terraform repository. The platform team reviews
the diff and teaches the workflow. It also keeps production controls in place.

That makes GitOps a platform practice, not just a tool choice. The data worker
doesn't become a full-time infrastructure specialist. The platform, SRE,
security, or [DataOps]({{ '/wiki/dataops/' | relative_url }}) team doesn't
disappear either.

Responsibility shifts toward guided self-service. The requester learns enough
Git, cloud, IAM, and [CI/CD]({{ '/wiki/ci-cd/' | relative_url }}) to make useful
changes. Reviewers keep the shared platform coherent.

## Guest Differences

Guests mostly differ on what should be managed through GitOps.

Tomasz focuses on infrastructure and developer enablement, with Terraform and
Terragrunt as examples. He also covers Atlantis and Docker images. CI runners,
IAM roles, and a migration from Jenkins to GitLab CI appear in the same episode
([DataOps and GitOps Best Practices for Data Teams]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }})).

His center of gravity is daily data-delivery friction because people need cloud
resources and reproducible environments. They also need a review path that
doesn't depend on local laptop state.

Bart applies the same reviewable-change workflow to governance. In
[Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }}),
he discusses access-as-code through Terraform, IAM, and pull requests. He also
warns that code alone doesn't solve governance.

As data products and consumers grow, teams still need ownership and
purpose-based requests. They also need approval workflows and revocation. This
connects GitOps to
[governance]({{ '/wiki/governance/' | relative_url }}) and
[data governance]({{ '/wiki/data-governance/' | relative_url }}) rather than
treating permissions as a pure engineering shortcut.

Maria's MLOps framing puts GitOps inside standardization. In
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}),
she emphasizes version control and reusable CI/CD. Registries and deployment
paths belong in the same foundation. Monitoring, authentication, and
standardized repositories do too.

Her pragmatic point is that many organizations already have Git and Kubernetes.
They also have orchestration and CI/CD, but product teams still struggle to use
those foundations consistently.

## Reviewable Infrastructure

The most concrete GitOps workflow in the archive is Tomasz's Terraform,
Terragrunt, and Atlantis example. A person creates a branch, edits
infrastructure code, and opens a merge request. Atlantis shows the planned
Terraform change before anything is applied in production
([DataOps and GitOps Best Practices for Data Teams]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }})).
The dangerous action becomes a diff, a plan, and a conversation.

That matters for data teams because infrastructure requests are often small but
blocking. A pipeline may need a storage bucket. A streaming use case may need a
topic or stream. A CI job may need a role. GitOps gives the platform team a
way to keep standards without turning every change into a private ticket queue.

It also gives analysts, data scientists, and data engineers a route into
platform work that's safer than running local Terraform with unclear
credentials.

The broader platform model also appears in
[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})'s
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
Simon discusses cloud infrastructure, Kubernetes, and Terraform. He also covers
deployment challenges and user-centered platform design.

His episode isn't only about GitOps. It reinforces the same boundary because
platform teams should understand data-science workflows and provide reusable
paths. They shouldn't expect every team to design production infrastructure
from scratch. See also
[MLOps]({{ '/wiki/mlops/' | relative_url }}),
[ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}), and
[Platform Adoption]({{ '/wiki/platform-adoption/' | relative_url }}).

## Access as Code

GitOps becomes governance work when the changed object is a permission rather
than a bucket or deployment. Bart explains that cloud data platforms remove many
of the old walls between source systems and downstream consumers. Lakes and
warehouses make that shared access easier
([Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }})).
As more people can reach shared data, dataset-level access management becomes a
platform responsibility.

Early access-as-code can look like Terraform, CloudFormation, IAM, and pull
requests. That gives teams reviewability and a durable audit trail. Bart's
warning is that access-as-code doesn't scale alone. The team also needs to know
who owns the dataset and why access is requested. It needs approvers, expiry,
and revocation.

This is where GitOps and [data governance]({{ '/wiki/data-governance/' | relative_url }})
meet. Git can store the permission change, but governance supplies the purpose,
ownership, and review process. [Security]({{ '/wiki/security/' | relative_url }})
supplies the risk boundary, especially when sensitive data, debugging access,
or privilege creep is involved.

## Reproducibility and Recovery

GitOps is useful only when the code path is reproducible. Tomasz connects
GitOps to fixed dependency versions and Docker images. He also links it to CI
migration and production data checks in
[DataOps and GitOps Best Practices for Data Teams]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }}).
He also warns that a green orchestrator status isn't enough if a job inserts
zero records. The platform needs versioned code, known environments, and checks
that match real data outcomes.

[Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }}) makes
the same DataOps argument from a reliability perspective in
[Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}).
He frames DataOps around reducing production errors, shortening deployment
cycles, and improving team productivity. Version control, tests, CI/CD,
and runbooks are part of the same operating system for reliable data delivery.
Observability and automation belong there too.

Maria extends the recovery story to ML delivery. In
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}),
version control and reusable CI/CD form the early maturity layer. Registries
and deployment templates belong there too. Monitoring, traceability, and
rollback extend that layer.

GitOps is therefore not "put everything in Git" as a slogan. It's the
combination of versioned desired state, automated checks, review, and
reproducible environments. It also gives teams a path back when a deployment or
data change goes wrong.

## Enablement and Team Design

The archive doesn't frame GitOps as self-service without support. Tomasz says
platform, SRE, security, and DataOps teams should guide and review changes.
That guidance matters when people first use Terraform, Terragrunt, or Atlantis.
It also matters around IAM and cloud resources
([DataOps and GitOps Best Practices for Data Teams]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }})).

Guidance can come through pairing and Slack support, while live coding,
templates, and documentation help too.

Maria describes a similar organization-level model for MLOps. A central team
provides standardized infrastructure, reusable CI/CD, and authentication.
Monitoring and templates help product teams avoid rebuilding the same delivery
machinery
([Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})).
That connects GitOps to [MLOps and DataOps]({{ '/wiki/mlops-and-dataops/' | relative_url }}):
both disciplines use automation and standard paths to make production work less
fragile.

The adoption risk is over-standardization. If the GitOps path is too abstract,
data teams avoid it and return to tickets or console edits. If it's too loose,
the platform loses security, reproducibility, and recovery. The useful middle
ground is a paved road with clear repositories, templates, plan output, and
documented approval paths. Humans should still be available when the diff isn't
obvious.

## Related Pages

These pages cover adjacent platform, governance, and delivery topics:

- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [MLOps and DataOps]({{ '/wiki/mlops-and-dataops/' | relative_url }})
- [CI/CD]({{ '/wiki/ci-cd/' | relative_url }})
- [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
- [Governance]({{ '/wiki/governance/' | relative_url }})
- [Security]({{ '/wiki/security/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})
- [Platform Adoption]({{ '/wiki/platform-adoption/' | relative_url }})
