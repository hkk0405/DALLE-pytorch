import math
import subprocess
import tqdm

aaa = '''
 images.a.a.tar application/octet-stream	2.19 GB		
  
 images.a.b.tar application/octet-stream	2.10 GB		
  
 images.a.c.tar application/octet-stream	2.31 GB		
  
 images.a.f.tar application/octet-stream	2.30 GB		
  
 images.a.g.tar application/octet-stream	2.15 GB		
  
 images.a.h.tar application/octet-stream	2.19 GB		
  
 images.a.i.tar	application/octet-stream	2.24 GB		
  
 images.a.j.tar	application/octet-stream	2.24 GB		
  
 images.a.k.tar	application/octet-stream	2.19 GB		
  
 images.a.l.tar	application/octet-stream	2.09 GB		
  
 images.a.m.tar	application/octet-stream	2.19 GB		
  
 images.a.n.tar	application/octet-stream	2.30 GB		
  
 images.a.o.tar	application/octet-stream	2.15 GB		
  
 images.a.p.tar	application/octet-stream	2.23 GB		
  
 images.a.q.tar	application/octet-stream	2.22 GB		
  
 images.a.r.tar	application/octet-stream	2.11 GB		
  
 images.a.s.tar	application/octet-stream	2.32 GB		
  
 images.a.t.tar	application/octet-stream	2.13 GB		
  
 images.a.u.tar	application/octet-stream	2.27 GB		
  
 images.a.v.tar	application/octet-stream	2.13 GB		
  
 images.a.w.tar	application/octet-stream	2.13 GB		
  
 images.a.x.tar	application/octet-stream	2.23 GB		
  
 images.a.y.tar	application/octet-stream	2.14 GB		
  
 images.a.z.tar	application/octet-stream	2.10 GB		
  
 images.b.a.tar	application/octet-stream	2.00 GB		
  
 images.b.b.tar	application/octet-stream	2.00 GB		
  
 images.b.c.tar	application/octet-stream	2.25 GB		
  
 images.b.d.tar	application/octet-stream	2.35 GB		
  
 images.b.e.tar	application/octet-stream	2.04 GB		
  
 images.b.f.tar	application/octet-stream	2.40 GB		
  
 images.b.g.tar	application/octet-stream	2.08 GB		
  
 images.b.h.tar	application/octet-stream	2.21 GB		
  
 images.b.i.tar	application/octet-stream	2.10 GB		
  
 images.b.j.tar	application/octet-stream	2.18 GB		
  
 images.b.k.tar	application/octet-stream	2.10 GB		
  
 images.b.l.tar	application/octet-stream	2.13 GB		
  
 images.b.m.tar	application/octet-stream	2.24 GB		
  
 images.b.n.tar	application/octet-stream	2.21 GB		
  
 images.b.o.tar	application/octet-stream	2.10 GB		
  
 images.b.p.tar	application/octet-stream	2.15 GB		
  
 images.b.q.tar	application/octet-stream	2.21 GB		
  
 images.b.r.tar	application/octet-stream	2.25 GB		
  
 images.b.s.tar	application/octet-stream	2.21 GB		
  
 images.b.t.tar	application/octet-stream	2.14 GB		
  
 images.b.u.tar	application/octet-stream	2.27 GB		
  
 images.b.v.tar	application/octet-stream	2.08 GB		
  
 images.b.w.tar	application/octet-stream	2.17 GB		
  
 images.b.x.tar	application/octet-stream	2.21 GB		
  
 images.b.y.tar	application/octet-stream	2.05 GB		
  
 images.b.z.tar	application/octet-stream	2.10 GB		
  
 images.c.a.tar	application/octet-stream	2.06 GB		
  
 images.c.b.tar	application/octet-stream	2.22 GB		
  
 images.c.c.tar	application/octet-stream	2.37 GB		
  
 images.c.d.tar	application/octet-stream	2.24 GB		
  
 images.c.e.tar	application/octet-stream	2.09 GB		
  
 images.c.f.tar	application/octet-stream	2.21 GB		
  
 images.c.g.tar	application/octet-stream	2.25 GB		
  
 images.c.h.tar	application/octet-stream	2.00 GB		
  
 images.c.i.tar	application/octet-stream	2.10 GB		
  
 images.c.j.tar	application/octet-stream	2.07 GB		
  
 images.c.k.tar	application/octet-stream	2.15 GB		
  
 images.c.l.tar	application/octet-stream	2.11 GB		
  
 images.c.m.tar	application/octet-stream	2.20 GB		
  
 images.c.n.tar	application/octet-stream	2.18 GB		
  
 images.c.o.tar	application/octet-stream	2.28 GB		
  
 images.c.p.tar	application/octet-stream	2.03 GB		
  
 images.c.q.tar	application/octet-stream	2.10 GB		
  
 images.c.r.tar	application/octet-stream	2.35 GB		
  
 images.c.s.tar	application/octet-stream	2.08 GB		
  
 images.c.t.tar	application/octet-stream	2.16 GB		
  
 images.c.u.tar	application/octet-stream	2.11 GB		
  
 images.c.v.tar	application/octet-stream	2.20 GB		
  
 images.c.w.tar	application/octet-stream	2.15 GB		
  
 images.c.x.tar	application/octet-stream	2.18 GB		
  
 images.c.y.tar	application/octet-stream	2.07 GB		
  
 images.c.z.tar	application/octet-stream	2.14 GB		
  
 images.d.a.tar	application/octet-stream	2.12 GB		
  
 images.d.b.tar	application/octet-stream	2.13 GB		
  
 images.d.c.tar	application/octet-stream	2.10 GB		
  
 images.d.d.tar	application/octet-stream	2.16 GB		
  
 images.d.e.tar	application/octet-stream	2.06 GB		
  
 images.d.f.tar	application/octet-stream	2.56 GB		
  
 images.d.g.tar	application/octet-stream	2.21 GB		
  
 images.d.h.tar	application/octet-stream	2.26 GB		
  
 images.d.i.tar	application/octet-stream	2.16 GB		
  
 images.d.j.tar	application/octet-stream	2.29 GB		
  
 images.d.k.tar	application/octet-stream	2.31 GB		
  
 images.d.l.tar	application/octet-stream	2.17 GB		
  
 images.d.m.tar	application/octet-stream	2.20 GB		
  
 images.d.n.tar	application/octet-stream	2.15 GB		
  
 images.d.o.tar	application/octet-stream	2.11 GB		
  
 images.d.p.tar	application/octet-stream	2.26 GB		
  
 images.d.q.tar	application/octet-stream	2.14 GB		
  
 images.d.r.tar	application/octet-stream	2.04 GB		
  
 images.d.s.tar	application/octet-stream	2.14 GB		
  
 images.d.t.tar	application/octet-stream	2.15 GB		
  
 images.d.u.tar	application/octet-stream	2.09 GB		
  
 images.d.v.tar	application/octet-stream	2.20 GB		
  
 images.d.w.tar	application/octet-stream	2.32 GB		
  
 images.d.x.tar	application/octet-stream	2.32 GB		
  
 images.d.y.tar	application/octet-stream	2.07 GB		
  
 images.d.z.tar	application/octet-stream	2.39 GB		
  
 images.e.a.tar	application/octet-stream	2.07 GB		
  
 images.e.b.tar	application/octet-stream	2.07 GB		
  
 images.e.c.tar	application/octet-stream	2.19 GB		
  
 images.e.d.tar	application/octet-stream	2.26 GB		
  
 images.e.e.tar	application/octet-stream	2.04 GB		
  
 images.e.f.tar	application/octet-stream	2.29 GB		
  
 images.e.g.tar	application/octet-stream	2.04 GB		
  
 images.e.h.tar	application/octet-stream	2.27 GB		
  
 images.e.i.tar	application/octet-stream	2.32 GB		
  
 images.e.j.tar	application/octet-stream	2.13 GB		
  
 images.e.k.tar	application/octet-stream	2.26 GB		
  
 images.e.l.tar	application/octet-stream	2.18 GB		
  
 images.e.m.tar	application/octet-stream	2.21 GB		
  
 images.e.n.tar	application/octet-stream	2.24 GB		
  
 images.e.o.tar	application/octet-stream	2.20 GB		
  
 images.e.p.tar	application/octet-stream	2.24 GB		
  
 images.e.q.tar	application/octet-stream	2.26 GB		
  
 images.e.r.tar	application/octet-stream	2.15 GB		
  
 images.e.s.tar	application/octet-stream	2.31 GB		
  
 images.e.t.tar	application/octet-stream	2.17 GB		
  
 images.e.u.tar	application/octet-stream	2.10 GB		
  
 images.e.v.tar	application/octet-stream	2.08 GB		
  
 images.e.w.tar	application/octet-stream	2.28 GB		
  
 images.e.x.tar	application/octet-stream	2.19 GB		
  
 images.e.y.tar	application/octet-stream	2.11 GB		
  
 images.e.z.tar	application/octet-stream	2.19 GB		
  
 images.f.a.tar	application/octet-stream	2.09 GB		
  
 images.f.b.tar	application/octet-stream	2.13 GB		
  
 images.f.c.tar	application/octet-stream	2.10 GB		
  
 images.f.d.tar	application/octet-stream	2.07 GB		
  
 images.f.e.tar	application/octet-stream	2.08 GB		
  
 images.f.f.tar	application/octet-stream	2.39 GB		
  
 images.f.g.tar	application/octet-stream	2.28 GB		
  
 images.f.h.tar	application/octet-stream	2.25 GB		
  
 images.f.i.tar	application/octet-stream	2.31 GB		
  
 images.f.j.tar	application/octet-stream	2.36 GB		
  
 images.f.k.tar	application/octet-stream	2.09 GB		
  
 images.f.l.tar	application/octet-stream	2.16 GB		
  
 images.f.m.tar	application/octet-stream	2.32 GB		
  
 images.f.n.tar	application/octet-stream	2.25 GB		
  
 images.f.o.tar	application/octet-stream	382.8 MB		
  
 images.f.p.tar	application/octet-stream	2.25 GB		
  
 images.f.q.tar	application/octet-stream	2.12 GB		
  
 images.f.r.tar	application/octet-stream	2.34 GB		
  
 images.f.s.tar	application/octet-stream	2.15 GB		
  
 images.f.t.tar	application/octet-stream	2.23 GB		
  
 images.f.u.tar	application/octet-stream	2.21 GB		
  
 images.f.v.tar	application/octet-stream	2.20 GB		
  
 images.f.w.tar	application/octet-stream	2.13 GB		
  
 images.f.x.tar	application/octet-stream	2.25 GB		
  
 images.f.y.tar	application/octet-stream	2.13 GB		
  
 images.f.z.tar	application/octet-stream	2.17 GB		
  
 images.g.a.tar	application/octet-stream	2.02 GB		
  
 images.g.b.tar	application/octet-stream	2.26 GB		
  
 images.g.c.tar	application/octet-stream	2.35 GB		
  
 images.g.d.tar	application/octet-stream	2.35 GB		
  
 images.g.e.tar	application/octet-stream	2.08 GB		
  
 images.g.f.tar	application/octet-stream	2.27 GB		
  
 images.g.g.tar	application/octet-stream	2.26 GB		
  
 images.g.h.tar	application/octet-stream	2.19 GB		
  
 images.g.i.tar	application/octet-stream	2.36 GB		
  
 images.g.j.tar	application/octet-stream	2.18 GB		
  
 images.g.k.tar	application/octet-stream	2.28 GB		
  
 images.g.l.tar	application/octet-stream	2.26 GB		
  
 images.g.m.tar	application/octet-stream	2.25 GB		
  
 images.g.n.tar	application/octet-stream	2.15 GB		
  
 images.g.o.tar	application/octet-stream	2.15 GB		
  
 images.g.p.tar	application/octet-stream	2.14 GB		
  
 images.g.q.tar	application/octet-stream	2.12 GB		
  
 images.g.r.tar	application/octet-stream	2.07 GB		
  
 images.g.s.tar	application/octet-stream	2.19 GB		
  
 images.g.t.tar	application/octet-stream	2.24 GB		
  
 images.g.u.tar	application/octet-stream	2.13 GB		
  
 images.g.v.tar	application/octet-stream	2.39 GB		
  
 images.g.w.tar	application/octet-stream	2.16 GB		
  
 images.g.x.tar	application/octet-stream	2.24 GB		
  
 images.g.y.tar	application/octet-stream	2.15 GB		
  
 images.g.z.tar	application/octet-stream	2.27 GB		
  
 images.h.a.tar	application/octet-stream	2.09 GB		
  
 images.h.b.tar	application/octet-stream	2.17 GB		
  
 images.h.c.tar	application/octet-stream	2.10 GB		
  
 images.h.d.tar	application/octet-stream	2.17 GB		
  
 images.h.e.tar	application/octet-stream	2.08 GB		
  
 images.h.f.tar	application/octet-stream	2.33 GB		
  
 images.h.g.tar	application/octet-stream	2.19 GB		
  
 images.h.h.tar	application/octet-stream	2.32 GB		
  
 images.h.i.tar	application/octet-stream	2.09 GB		
  
 images.h.j.tar	application/octet-stream	2.27 GB		
  
 images.h.k.tar	application/octet-stream	2.20 GB		
  
 images.h.l.tar	application/octet-stream	2.13 GB		
  
 images.h.m.tar	application/octet-stream	2.22 GB		
  
 images.h.n.tar	application/octet-stream	2.10 GB		
  
 images.h.o.tar	application/octet-stream	2.26 GB		
  
 images.h.p.tar	application/octet-stream	2.11 GB		
  
 images.h.q.tar	application/octet-stream	2.07 GB		
  
 images.h.r.tar	application/octet-stream	2.15 GB		
  
 images.h.s.tar	application/octet-stream	2.39 GB		
  
 images.h.t.tar	application/octet-stream	2.25 GB		
  
 images.h.u.tar	application/octet-stream	2.33 GB		
  
 images.h.v.tar	application/octet-stream	2.10 GB		
  
 images.h.w.tar	application/octet-stream	2.04 GB		
  
 images.h.x.tar	application/octet-stream	2.23 GB		
  
 images.h.y.tar	application/octet-stream	2.27 GB		
  
 images.h.z.tar	application/octet-stream	2.28 GB		
  
 images.i.a.tar	application/octet-stream	2.03 GB		
  
 images.i.b.tar	application/octet-stream	2.14 GB		
  
 images.i.c.tar	application/octet-stream	2.15 GB		
  
 images.i.d.tar	application/octet-stream	2.09 GB		
  
 images.i.e.tar	application/octet-stream	2.02 GB		
  
 images.i.f.tar	application/octet-stream	2.25 GB		
  
 images.i.g.tar	application/octet-stream	2.22 GB		
  
 images.i.h.tar	application/octet-stream	2.12 GB		
  
 images.i.i.tar	application/octet-stream	2.21 GB		
  
 images.i.j.tar	application/octet-stream	2.19 GB		
  
 images.i.k.tar	application/octet-stream	2.16 GB		
  
 images.i.l.tar	application/octet-stream	2.05 GB		
  
 images.i.m.tar	application/octet-stream	2.18 GB		
  
 images.i.n.tar	application/octet-stream	2.27 GB		
  
 images.i.o.tar	application/octet-stream	2.29 GB		
  
 images.i.p.tar	application/octet-stream	2.13 GB		
  
 images.i.q.tar	application/octet-stream	2.13 GB		
  
 images.i.r.tar	application/octet-stream	2.12 GB		
  
 images.i.s.tar	application/octet-stream	2.24 GB		
  
 images.i.t.tar	application/octet-stream	2.13 GB		
  
 images.i.u.tar	application/octet-stream	2.24 GB		
  
 images.i.v.tar	application/octet-stream	2.13 GB		
  
 images.i.w.tar	application/octet-stream	2.25 GB		
  
 images.i.x.tar	application/octet-stream	2.18 GB		
  
 images.i.y.tar	application/octet-stream	2.15 GB		
  
 images.i.z.tar	application/octet-stream	2.24 GB		
  
 images.j.a.tar	application/octet-stream	2.17 GB		
  
 images.j.b.tar	application/octet-stream	2.16 GB		
  
 images.j.c.tar	application/octet-stream	2.32 GB		
  
 images.j.d.tar	application/octet-stream	2.11 GB		
  
 images.j.e.tar	application/octet-stream	2.17 GB		
  
 images.j.f.tar	application/octet-stream	2.26 GB		
  
 images.j.g.tar	application/octet-stream	2.38 GB		
  
 images.j.h.tar	application/octet-stream	2.27 GB		
  
 images.j.i.tar	application/octet-stream	2.16 GB		
  
 images.j.j.tar	application/octet-stream	2.16 GB		
  
 images.j.k.tar	application/octet-stream	2.24 GB		
  
 images.j.l.tar	application/octet-stream	2.06 GB		
  
 images.j.m.tar	application/octet-stream	2.36 GB		
  
 images.j.n.tar	application/octet-stream	2.07 GB		
  
 images.j.o.tar	application/octet-stream	2.32 GB		
  
 images.j.p.tar	application/octet-stream	2.12 GB		
  
 images.j.q.tar	application/octet-stream	2.07 GB		
  
 images.j.r.tar	application/octet-stream	2.16 GB		
  
 images.j.s.tar	application/octet-stream	2.19 GB		
  
 images.j.t.tar	application/octet-stream	2.41 GB		
  
 images.j.u.tar	application/octet-stream	2.19 GB		
  
 images.j.v.tar	application/octet-stream	2.24 GB		
  
 images.j.w.tar	application/octet-stream	2.18 GB		
  
 images.j.x.tar	application/octet-stream	2.17 GB		
  
 images.j.y.tar	application/octet-stream	2.20 GB		
  
 images.j.z.tar	application/octet-stream	2.21 GB		
  
 images.k.a.tar	application/octet-stream	1.95 GB		
  
 images.k.b.tar	application/octet-stream	2.03 GB		
  
 images.k.c.tar	application/octet-stream	2.01 GB		
  
 images.k.d.tar	application/octet-stream	2.17 GB		
  
 images.k.e.tar	application/octet-stream	2.34 GB		
  
 images.k.f.tar	application/octet-stream	2.07 GB		
  
 images.k.g.tar	application/octet-stream	2.09 GB		
  
 images.k.h.tar	application/octet-stream	2.45 GB		
  
 images.k.i.tar	application/octet-stream	2.18 GB		
  
 images.k.j.tar	application/octet-stream	2.05 GB		
  
 images.k.k.tar	application/octet-stream	2.23 GB		
  
 images.k.l.tar	application/octet-stream	2.11 GB		
  
 images.k.m.tar	application/octet-stream	2.38 GB		
  
 images.k.n.tar	application/octet-stream	2.04 GB		
  
 images.k.o.tar	application/octet-stream	2.11 GB		
  
 images.k.p.tar	application/octet-stream	2.05 GB		
  
 images.k.q.tar	application/octet-stream	1.88 GB		
  
 images.k.r.tar	application/octet-stream	2.12 GB		
  
 images.k.s.tar	application/octet-stream	2.11 GB		
  
 images.k.t.tar	application/octet-stream	1.98 GB		
  
 images.k.u.tar	application/octet-stream	2.20 GB		
  
 images.k.v.tar	application/octet-stream	2.09 GB		
  
 images.k.w.tar	application/octet-stream	2.08 GB		
  
 images.k.x.tar	application/octet-stream	2.07 GB		
  
 images.k.y.tar	application/octet-stream	2.01 GB		
  
 images.k.z.tar	application/octet-stream	2.11 GB		
  
 images.l.a.tar	application/octet-stream	1.95 GB		
  
 images.l.b.tar	application/octet-stream	2.27 GB		
  
 images.l.c.tar	application/octet-stream	1.96 GB		
  
 images.l.d.tar	application/octet-stream	1.97 GB		
  
 images.l.e.tar	application/octet-stream	2.17 GB		
  
 images.l.f.tar	application/octet-stream	2.15 GB		
  
 images.l.g.tar	application/octet-stream	2.00 GB		
  
 images.l.h.tar	application/octet-stream	1.98 GB		
  
 images.l.i.tar	application/octet-stream	2.01 GB		
  
 images.l.j.tar	application/octet-stream	2.10 GB		
  
 images.l.k.tar	application/octet-stream	2.07 GB		
  
 images.l.l.tar	application/octet-stream	2.08 GB		
  
 images.l.m.tar	application/octet-stream	2.10 GB		
  
 images.l.n.tar	application/octet-stream	2.03 GB		
  
 images.l.o.tar	application/octet-stream	2.16 GB		
  
 images.l.p.tar	application/octet-stream	2.00 GB		
  
 images.l.q.tar	application/octet-stream	2.08 GB		
  
 images.l.r.tar	application/octet-stream	2.11 GB		
  
 images.l.s.tar	application/octet-stream	2.18 GB		
  
 images.l.t.tar	application/octet-stream	2.18 GB		
  
 images.l.u.tar	application/octet-stream	2.32 GB		
  
 images.l.v.tar	application/octet-stream	2.05 GB		
  
 images.l.w.tar	application/octet-stream	2.14 GB		
  
 images.l.x.tar	application/octet-stream	2.10 GB		
  
 images.l.y.tar	application/octet-stream	2.15 GB		
  
 images.l.z.tar	application/octet-stream	2.06 GB		
  
 images.m.a.tar	application/octet-stream	2.11 GB		
  
 images.m.b.tar	application/octet-stream	2.18 GB		
  
 images.m.c.tar	application/octet-stream	1.97 GB		
  
 images.m.d.tar	application/octet-stream	2.01 GB		
  
 images.m.e.tar	application/octet-stream	2.06 GB		
  
 images.m.f.tar	application/octet-stream	2.17 GB		
  
 images.m.g.tar	application/octet-stream	2.08 GB		
  
 images.m.h.tar	application/octet-stream	2.13 GB		
  
 images.m.i.tar	application/octet-stream	2.08 GB		
  
 images.m.j.tar	application/octet-stream	2.14 GB		
  
 images.m.k.tar	application/octet-stream	2.14 GB		
  
 images.m.l.tar	application/octet-stream	2.23 GB		
  
 images.m.m.tar	application/octet-stream	1.96 GB		
  
 images.m.n.tar	application/octet-stream	2.15 GB		
  
 images.m.o.tar	application/octet-stream	2.06 GB		
  
 images.m.p.tar	application/octet-stream	2.24 GB		
  
 images.m.q.tar	application/octet-stream	2.09 GB		
  
 images.m.r.tar	application/octet-stream	2.19 GB		
  
 images.m.s.tar	application/octet-stream	2.11 GB		
  
 images.m.t.tar	application/octet-stream	2.06 GB		
  
 images.m.u.tar	application/octet-stream	2.13 GB		
  
 images.m.v.tar	application/octet-stream	2.07 GB		
  
 images.m.w.tar	application/octet-stream	2.23 GB		
  
 images.m.x.tar	application/octet-stream	2.07 GB		
  
 images.m.y.tar	application/octet-stream	2.16 GB		
  
 images.m.z.tar	application/octet-stream	2.24 GB		
  
 images.n.a.tar	application/octet-stream	2.14 GB		
  
 images.n.b.tar	application/octet-stream	2.09 GB		
  
 images.n.c.tar	application/octet-stream	2.08 GB		
  
 images.n.d.tar	application/octet-stream	2.08 GB		
  
 images.n.e.tar	application/octet-stream	2.15 GB		
  
 images.n.f.tar	application/octet-stream	2.11 GB		
  
 images.n.g.tar	application/octet-stream	1.97 GB		
  
 images.n.h.tar	application/octet-stream	2.26 GB		
  
 images.n.i.tar	application/octet-stream	2.23 GB		
  
 images.n.j.tar	application/octet-stream	2.10 GB		
  
 images.n.k.tar	application/octet-stream	2.01 GB		
  
 images.n.l.tar	application/octet-stream	2.07 GB		
  
 images.n.m.tar	application/octet-stream	1.98 GB		
  
 images.n.n.tar	application/octet-stream	1.95 GB		
  
 images.n.o.tar	application/octet-stream	2.10 GB		
  
 images.n.p.tar	application/octet-stream	2.08 GB		
  
 images.n.q.tar	application/octet-stream	2.07 GB		
  
 images.n.r.tar	application/octet-stream	1.98 GB		
  
 images.n.s.tar	application/octet-stream	1.94 GB		
  
 images.n.t.tar	application/octet-stream	2.17 GB		
  
 images.n.u.tar	application/octet-stream	2.11 GB		
  
 images.n.v.tar	application/octet-stream	2.30 GB		
  
 images.n.w.tar	application/octet-stream	1.95 GB		
  
 images.n.x.tar	application/octet-stream	2.14 GB		
  
 images.n.y.tar	application/octet-stream	2.05 GB		
  
 images.n.z.tar	application/octet-stream	2.26 GB		
  
 images.o.a.tar	application/octet-stream	2.10 GB		
  
 images.o.b.tar	application/octet-stream	2.20 GB		
  
 images.o.c.tar	application/octet-stream	2.09 GB		
  
 images.o.d.tar	application/octet-stream	2.27 GB		
  
 images.o.e.tar	application/octet-stream	2.10 GB		
  
 images.o.f.tar	application/octet-stream	2.16 GB		
  
 images.o.g.tar	application/octet-stream	2.05 GB		
  
 images.o.h.tar	application/octet-stream	2.26 GB		
  
 images.o.i.tar	application/octet-stream	2.10 GB		
  
 images.o.j.tar	application/octet-stream	2.08 GB		
  
 images.o.k.tar	application/octet-stream	1.96 GB		
  
 images.o.l.tar	application/octet-stream	2.05 GB		
  
 images.o.m.tar	application/octet-stream	2.02 GB		
  
 images.o.n.tar	application/octet-stream	2.02 GB		
  
 images.o.o.tar	application/octet-stream	2.05 GB		
  
 images.o.p.tar	application/octet-stream	2.00 GB		
  
 images.o.q.tar	application/octet-stream	1.98 GB		
  
 images.o.r.tar	application/octet-stream	2.15 GB		
  
 images.o.s.tar	application/octet-stream	2.05 GB		
  
 images.o.t.tar	application/octet-stream	2.13 GB		
  
 images.o.u.tar	application/octet-stream	2.21 GB		
  
 images.o.v.tar	application/octet-stream	2.17 GB		
  
 images.o.w.tar	application/octet-stream	2.11 GB		
  
 images.o.x.tar	application/octet-stream	2.16 GB		
  
 images.o.y.tar	application/octet-stream	2.23 GB		
  
 images.o.z.tar	application/octet-stream	2.06 GB		
  
 images.p.a.tar	application/octet-stream	2.15 GB		
  
 images.p.b.tar	application/octet-stream	2.15 GB		
  
 images.p.c.tar	application/octet-stream	2.05 GB		
  
 images.p.d.tar	application/octet-stream	2.13 GB		
  
 images.p.e.tar	application/octet-stream	2.07 GB		
  
 images.p.f.tar	application/octet-stream	2.09 GB		
  
 images.p.g.tar	application/octet-stream	2.19 GB		
  
 images.p.h.tar	application/octet-stream	2.20 GB		
  
 images.p.i.tar	application/octet-stream	2.17 GB		
  
 images.p.j.tar	application/octet-stream	1.99 GB		
  
 images.p.k.tar	application/octet-stream	2.09 GB		
  
 images.p.l.tar	application/octet-stream	2.22 GB		
  
 images.p.m.tar	application/octet-stream	1.96 GB		
  
 images.p.n.tar	application/octet-stream	1.98 GB		
  
 images.p.o.tar	application/octet-stream	1.93 GB		
  
 images.p.p.tar	application/octet-stream	1.96 GB		
  
 images.p.q.tar	application/octet-stream	2.05 GB		
  
 images.p.r.tar	application/octet-stream	2.06 GB		
  
 images.p.s.tar	application/octet-stream	2.10 GB		
  
 images.p.t.tar	application/octet-stream	2.03 GB		
  
 images.p.u.tar	application/octet-stream	2.19 GB		
  
 images.p.v.tar	application/octet-stream	2.23 GB		
  
 images.p.w.tar	application/octet-stream	2.01 GB		
  
 images.p.x.tar	application/octet-stream	2.17 GB		
  
 images.p.y.tar	application/octet-stream	2.09 GB		
  
 images.p.z.tar	application/octet-stream	2.17 GB		
  
 images.q.a.tar	application/octet-stream	2.03 GB		
  
 images.q.b.tar	application/octet-stream	2.01 GB		
  
 images.q.c.tar	application/octet-stream	1.96 GB		
  
 images.q.d.tar	application/octet-stream	2.16 GB		
  
 images.q.e.tar	application/octet-stream	2.35 GB		
  
 images.q.f.tar	application/octet-stream	2.09 GB		
  
 images.q.g.tar	application/octet-stream	2.10 GB		
  
 images.q.h.tar	application/octet-stream	2.20 GB		
  
 images.q.i.tar	application/octet-stream	1.99 GB		
  
 images.q.j.tar	application/octet-stream	2.02 GB		
  
 images.q.k.tar	application/octet-stream	2.04 GB		
  
 images.q.l.tar	application/octet-stream	2.25 GB		
  
 images.q.m.tar	application/octet-stream	1.98 GB		
  
 images.q.n.tar	application/octet-stream	2.11 GB		
  
 images.q.o.tar	application/octet-stream	2.19 GB		
  
 images.q.p.tar	application/octet-stream	2.07 GB		
  
 images.q.q.tar	application/octet-stream	2.08 GB		
  
 images.q.r.tar	application/octet-stream	2.06 GB		
  
 images.q.s.tar	application/octet-stream	2.18 GB		
  
 images.q.t.tar	application/octet-stream	2.24 GB		
  
 images.q.u.tar	application/octet-stream	2.01 GB		
  
 images.q.v.tar	application/octet-stream	2.51 GB		
  
 images.q.w.tar	application/octet-stream	2.06 GB		
  
 images.q.x.tar	application/octet-stream	2.16 GB		
  
 images.q.y.tar	application/octet-stream	2.06 GB		
  
 images.q.z.tar	application/octet-stream	2.06 GB		
  
 images.r.a.tar	application/octet-stream	2.05 GB		
  
 images.r.b.tar	application/octet-stream	2.11 GB		
  
 images.r.c.tar	application/octet-stream	2.07 GB		
  
 images.r.d.tar	application/octet-stream	2.15 GB		
  
 images.r.e.tar	application/octet-stream	2.14 GB		
  
 images.r.f.tar	application/octet-stream	2.14 GB		
  
 images.r.g.tar	application/octet-stream	2.21 GB		
  
 images.r.h.tar	application/octet-stream	2.27 GB		
  
 images.r.i.tar	application/octet-stream	1.93 GB		
  
 images.r.j.tar	application/octet-stream	1.95 GB		
  
 images.r.k.tar	application/octet-stream	2.14 GB		
  
 images.r.l.tar	application/octet-stream	2.19 GB		
  
 images.r.m.tar	application/octet-stream	2.07 GB		
  
 images.r.n.tar	application/octet-stream	2.09 GB		
  
 images.r.o.tar	application/octet-stream	2.25 GB		
  
 images.r.p.tar	application/octet-stream	1.98 GB		
  
 images.r.q.tar	application/octet-stream	2.05 GB		
  
 images.r.r.tar	application/octet-stream	2.13 GB		
  
 images.r.s.tar	application/octet-stream	2.21 GB		
  
 images.r.t.tar	application/octet-stream	2.13 GB		
  
 images.r.u.tar	application/octet-stream	2.08 GB		
  
 images.r.v.tar	application/octet-stream	2.42 GB		
  
 images.r.w.tar	application/octet-stream	2.00 GB		
  
 images.r.x.tar	application/octet-stream	2.05 GB		
  
 images.r.y.tar	application/octet-stream	1.97 GB		
  
 images.r.z.tar	application/octet-stream	1.92 GB		
  
 images.t.a.tar	application/octet-stream	2.07 GB		
  
 images.t.b.tar	application/octet-stream	2.16 GB		
  
 images.t.c.tar	application/octet-stream	2.08 GB		
  
 images.t.d.tar	application/octet-stream	2.20 GB		
  
 images.t.e.tar	application/octet-stream	2.11 GB		
  
 images.t.f.tar	application/octet-stream	1.95 GB		
  
 images.t.g.tar	application/octet-stream	2.33 GB		
  
 images.t.h.tar	application/octet-stream	2.21 GB		
  
 images.t.i.tar	application/octet-stream	1.96 GB		
  
 images.t.j.tar	application/octet-stream	2.12 GB		
  
 images.t.k.tar	application/octet-stream	2.07 GB		
  
 images.t.l.tar	application/octet-stream	1.97 GB		
  
 images.t.m.tar	application/octet-stream	2.02 GB		
  
 images.t.n.tar	application/octet-stream	2.12 GB		
  
 images.t.o.tar	application/octet-stream	2.31 GB		
  
 images.t.p.tar	application/octet-stream	1.93 GB		
  
 images.t.q.tar	application/octet-stream	2.03 GB		
  
 images.t.r.tar	application/octet-stream	2.08 GB		
  
 images.t.s.tar	application/octet-stream	2.04 GB		
  
 images.t.t.tar	application/octet-stream	2.17 GB		
  
 images.t.u.tar	application/octet-stream	2.15 GB		
  
 images.t.v.tar	application/octet-stream	2.28 GB		
  
 images.t.w.tar	application/octet-stream	2.13 GB		
  
 images.t.x.tar	application/octet-stream	2.11 GB		
  
 images.t.y.tar	application/octet-stream	2.11 GB		
  
 images.t.z.tar	application/octet-stream	2.01 GB		
  
 images.u.a.tar	application/octet-stream	2.10 GB		
  
 images.u.b.tar	application/octet-stream	2.15 GB		
  
 images.u.c.tar	application/octet-stream	2.07 GB		
  
 images.u.d.tar	application/octet-stream	2.09 GB		
  
 images.u.e.tar	application/octet-stream	2.16 GB		
  
 images.u.f.tar	application/octet-stream	2.05 GB		
  
 images.u.g.tar	application/octet-stream	2.18 GB		
  
 images.u.h.tar	application/octet-stream	2.16 GB		
  
 images.u.i.tar	application/octet-stream	2.00 GB		
  
 images.u.j.tar	application/octet-stream	2.03 GB		
  
 images.u.k.tar	application/octet-stream	2.01 GB		
  
 images.u.l.tar	application/octet-stream	2.09 GB		
  
 images.u.m.tar	application/octet-stream	2.11 GB		
  
 images.u.n.tar	application/octet-stream	2.12 GB		
  
 images.u.o.tar	application/octet-stream	2.21 GB		
  
 images.u.p.tar	application/octet-stream	2.03 GB		
  
 images.u.q.tar	application/octet-stream	1.95 GB		
  
 images.u.r.tar	application/octet-stream	2.03 GB		
  
 images.u.s.tar	application/octet-stream	2.12 GB		
  
 images.u.t.tar	application/octet-stream	2.16 GB		
  
 images.u.u.tar	application/octet-stream	1.92 GB		
  
 images.u.v.tar	application/octet-stream	2.21 GB		
  
 images.u.w.tar	application/octet-stream	2.03 GB		
  
 images.u.x.tar	application/octet-stream	2.01 GB		
  
 images.u.y.tar	application/octet-stream	2.44 GB		
  
 images.u.z.tar	application/octet-stream	2.13 GB		
  
 images.v.a.tar	application/octet-stream	2.08 GB		
  
 images.v.b.tar	application/octet-stream	2.20 GB		
  
 images.v.c.tar	application/octet-stream	1.97 GB		
  
 images.v.d.tar	application/octet-stream	1.93 GB		
  
 images.v.e.tar	application/octet-stream	2.09 GB		
  
 images.v.f.tar	application/octet-stream	2.07 GB		
  
 images.v.g.tar	application/octet-stream	2.03 GB		
  
 images.v.h.tar	application/octet-stream	2.04 GB		
  
 images.v.i.tar	application/octet-stream	2.24 GB		
  
 images.v.j.tar	application/octet-stream	2.10 GB		
  
 images.v.k.tar	application/octet-stream	2.15 GB		
  
 images.v.l.tar	application/octet-stream	2.04 GB		
  
 images.v.m.tar	application/octet-stream	2.08 GB		
  
 images.v.n.tar	application/octet-stream	2.00 GB		
  
 images.v.o.tar	application/octet-stream	2.16 GB		
  
 images.v.p.tar	application/octet-stream	2.13 GB		
  
 images.v.q.tar	application/octet-stream	2.03 GB		
  
 images.v.r.tar	application/octet-stream	2.15 GB		
  
 images.v.s.tar	application/octet-stream	2.15 GB		
  
 images.v.t.tar	application/octet-stream	2.05 GB		
  
 images.v.u.tar	application/octet-stream	2.18 GB		
  
 images.v.v.tar	application/octet-stream	2.25 GB		
  
 images.v.w.tar	application/octet-stream	2.04 GB		
  
 images.v.x.tar	application/octet-stream	2.09 GB		
  
 images.v.y.tar	application/octet-stream	2.09 GB		
  
 images.v.z.tar	application/octet-stream	2.11 GB		
  
 images.w.a.tar	application/octet-stream	2.07 GB		
  
 images.w.b.tar	application/octet-stream	2.23 GB		
  
 images.w.c.tar	application/octet-stream	2.09 GB		
  
 images.w.d.tar	application/octet-stream	1.93 GB		
  
 images.w.e.tar	application/octet-stream	2.19 GB		
  
 images.w.f.tar	application/octet-stream	2.10 GB		
  
 images.w.g.tar	application/octet-stream	2.07 GB		
  
 images.w.h.tar	application/octet-stream	1.99 GB		
  
 images.w.i.tar	application/octet-stream	2.24 GB		
  
 images.w.j.tar	application/octet-stream	2.07 GB		
  
 images.w.k.tar	application/octet-stream	2.10 GB		
  
 images.w.l.tar	application/octet-stream	2.03 GB		
  
 images.w.m.tar	application/octet-stream	2.02 GB		
  
 images.w.n.tar	application/octet-stream	2.13 GB		
  
 images.w.o.tar	application/octet-stream	2.24 GB		
  
 images.w.p.tar	application/octet-stream	2.20 GB		
  
 images.w.q.tar	application/octet-stream	2.07 GB		
  
 images.w.r.tar	application/octet-stream	2.48 GB		
  
 images.w.s.tar	application/octet-stream	1.96 GB		
  
 images.w.t.tar	application/octet-stream	2.19 GB		
  
 images.w.u.tar	application/octet-stream	2.09 GB		
  
 images.w.v.tar	application/octet-stream	2.19 GB		
  
 images.w.w.tar	application/octet-stream	2.17 GB		
  
 images.w.x.tar	application/octet-stream	2.15 GB		
  
 images.w.y.tar	application/octet-stream	2.17 GB		
  
 images.w.z.tar	application/octet-stream	2.00 GB		
  
 images.x.a.tar	application/octet-stream	1.97 GB		
  
 images.x.b.tar	application/octet-stream	2.17 GB		
  
 images.x.c.tar	application/octet-stream	2.21 GB		
  
 images.x.d.tar	application/octet-stream	1.97 GB		
  
 images.x.e.tar	application/octet-stream	2.07 GB		
  
 images.x.f.tar	application/octet-stream	2.05 GB		
  
 images.x.g.tar	application/octet-stream	1.95 GB		
  
 images.x.h.tar	application/octet-stream	2.06 GB		
  
 images.x.i.tar	application/octet-stream	2.21 GB		
  
 images.x.j.tar	application/octet-stream	2.08 GB		
  
 images.x.k.tar	application/octet-stream	2.17 GB		
  
 images.x.l.tar	application/octet-stream	2.03 GB		
  
 images.x.m.tar	application/octet-stream	2.11 GB		
  
 images.x.n.tar	application/octet-stream	2.14 GB		
  
 images.x.o.tar	application/octet-stream	2.17 GB		
  
 images.x.p.tar	application/octet-stream	1.96 GB		
  
 images.x.q.tar	application/octet-stream	2.06 GB		
  
 images.x.r.tar	application/octet-stream	2.14 GB		
  
 images.x.s.tar	application/octet-stream	2.00 GB		
  
 images.x.t.tar	application/octet-stream	2.23 GB		
  
 images.x.u.tar	application/octet-stream	2.09 GB		
  
 images.x.v.tar	application/octet-stream	2.20 GB		
  
 images.x.w.tar	application/octet-stream	2.17 GB		
  
 images.x.x.tar	application/octet-stream	2.02 GB		
  
 images.x.y.tar	application/octet-stream	2.12 GB		
  
 images.x.z.tar	application/octet-stream	1.98 GB		
  
 images.y.a.tar	application/octet-stream	2.22 GB		
  
 images.y.b.tar	application/octet-stream	2.18 GB		
  
 images.y.c.tar	application/octet-stream	2.11 GB		
  
 images.y.d.tar	application/octet-stream	2.05 GB		
  
 images.y.e.tar	application/octet-stream	2.37 GB		
  
 images.y.f.tar	application/octet-stream	2.14 GB		
  
 images.y.g.tar	application/octet-stream	2.06 GB		
  
 images.y.h.tar	application/octet-stream	2.20 GB		
  
 images.y.i.tar	application/octet-stream	2.18 GB		
  
 images.y.j.tar	application/octet-stream	2.16 GB		
  
 images.y.k.tar	application/octet-stream	2.11 GB		
  
 images.y.l.tar	application/octet-stream	1.98 GB		
  
 images.y.m.tar	application/octet-stream	2.06 GB		
  
 images.y.n.tar	application/octet-stream	1.99 GB		
  
 images.y.o.tar	application/octet-stream	2.10 GB		
  
 images.y.p.tar	application/octet-stream	2.00 GB		
  
 images.y.q.tar	application/octet-stream	1.86 GB		
  
 images.y.r.tar	application/octet-stream	2.07 GB		
  
 images.y.s.tar	application/octet-stream	2.06 GB		
  
 images.y.t.tar	application/octet-stream	2.31 GB		
  
 images.y.u.tar	application/octet-stream	1.97 GB		
  
 images.y.v.tar	application/octet-stream	2.01 GB		
  
 images.y.w.tar	application/octet-stream	2.18 GB		
  
 images.y.x.tar	application/octet-stream	2.19 GB		
  
 images.y.y.tar	application/octet-stream	2.33 GB		
  
 images.y.z.tar	application/octet-stream	1.98 GB		
  
 images.z.a.tar	application/octet-stream	2.02 GB		
  
 images.z.b.tar	application/octet-stream	2.18 GB		
  
 images.z.c.tar	application/octet-stream	2.03 GB		
  
 images.z.d.tar	application/octet-stream	2.00 GB		
  
 images.z.e.tar	application/octet-stream	2.46 GB		
  
 images.z.f.tar	application/octet-stream	2.15 GB		
  
 images.z.g.tar	application/octet-stream	1.96 GB		
  
 images.z.h.tar	application/octet-stream	2.38 GB		
  
 images.z.i.tar	application/octet-stream	2.14 GB		
  
 images.z.j.tar	application/octet-stream	2.15 GB		
  
 images.z.k.tar	application/octet-stream	1.88 GB		
  
 images.z.l.tar	application/octet-stream	2.02 GB		
  
 images.z.m.tar	application/octet-stream	1.97 GB		
  
 images.z.n.tar	application/octet-stream	2.05 GB		
  
 images.z.o.tar	application/octet-stream	2.20 GB		
  
 images.z.p.tar	application/octet-stream	1.67 GB		
  
 images.z.q.tar	application/octet-stream	1.96 GB		
  
 images.z.r.tar	application/octet-stream	2.24 GB		
  
 images.z.s.tar	application/octet-stream	1.94 GB		
  
 images.z.t.tar	application/octet-stream	2.34 GB		
  
 images.z.u.tar	application/octet-stream	1.98 GB		
  
 images.z.v.tar	application/octet-stream	2.14 GB		
  
 images.z.w.tar	application/octet-stream	2.02 GB		
  
 images.z.x.tar	application/octet-stream	2.03 GB		
  
 images.z.y.tar	application/octet-stream	2.20 GB		
  
 images.z.z.tar	application/octet-stream	2.17 GB		
  
 SHA256SUMS	application/octet-stream	59.0 kB		
  
 cdip-1.tar	application/octet-stream	4.68 GB		
  
 cdip-2.tar	application/octet-stream	4.70 GB		
  
 cdip-3.tar	application/octet-stream	4.69 GB		
  
 cdip-4.tar	application/octet-stream	4.67 GB		
  
 cdip-5.tar	application/octet-stream	4.68 GB		
  
 cdip-6.tar	application/octet-stream	292.4 MB		
  
 SHA256SUMS	application/octet-stream	462 Bytes		
  
'''

download_path = '/disk/nvme2/iit_cdip'

download_fs = aaa.split('\n')[1:-1]
imgs = [f'wget -P {download_path}/cdip-images https://data.nist.gov/od/ds/ark:/88434/mds2-2531/cdip-images/{i.split("application/octet-stream")[0].strip()}' for i in download_fs[:-7]]
txts = [f'wget -P {download_path}/cdip-text https://data.nist.gov/od/ds/ark:/88434/mds2-2531/cdip-text/{i.split("application/octet-stream")[0].strip()}' for i in download_fs[-7:]]

download_img_cmds = [' & '.join(imgs[i*3:(i+1)*3]) for i in range(math.ceil(len(imgs)/3))]
for i in tqdm.tqdm(download_img_cmds):
    subprocess.run(i, shell=True)

download_txt_cmds = [' & '.join(txts[i*3:(i+1)*3]) for i in range(math.ceil(len(txts)/3))]
for i in tqdm.tqdm(download_txt_cmds):
    subprocess.run(i, shell=True)
