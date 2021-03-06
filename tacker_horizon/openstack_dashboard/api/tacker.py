# Copyright 2015 Brocade Communications System, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from __future__ import absolute_import

from django.conf import settings
from oslo_log import log as logging
from tackerclient.v1_0 import client as tacker_client

from horizon.utils.memoized import memoized  # noqa
from openstack_dashboard.api import base


LOG = logging.getLogger(__name__)


@memoized
def tackerclient(request):
    insecure = getattr(settings, 'OPENSTACK_SSL_NO_VERIFY', False)
    cacert = getattr(settings, 'OPENSTACK_SSL_CACERT', None)
    c = tacker_client.Client(
        token=request.user.token.id,
        auth_url=base.url_for(request, 'identity'),
        endpoint_url=base.url_for(request, 'nfv-orchestration'),
        insecure=insecure, ca_cert=cacert)
    return c


def vnf_list(request, **params):
    LOG.debug("vnf_list(): params=%s", params)
    vnfs = tackerclient(request).list_vnfs(**params).get('vnfs')
    return vnfs


def vnfd_list(request, **params):
    LOG.debug("vnfd_list(): params=%s", params)
    vnfds = tackerclient(request).list_vnfds(**params).get('vnfds')
    return vnfds


def create_vnfd(request, tosca_body=None, **params):
    LOG.debug("create_vnfd(): params=%s", params)
    vnfd_instance = tackerclient(request).create_vnfd(body=tosca_body)
    return vnfd_instance


def create_vnf(request, vnf_arg, **params):
    LOG.debug("create_vnf(): vnf_arg=%s", str(vnf_arg))
    vnf_instance = tackerclient(request).create_vnf(body=vnf_arg)
    return vnf_instance


def get_vnfd(request, vnfd_id):
    LOG.debug("vnfd_get(): vnfd_id=%s", str(vnfd_id))
    vnfd = tackerclient(request).show_vnfd(vnfd_id)
    return vnfd


def get_vnf(request, vnf_id):
    LOG.debug("vnf_get(): vnf_id=%s", str(vnf_id))
    vnf_instance = tackerclient(request).show_vnf(vnf_id)
    return vnf_instance


def delete_vnf(request, vnf_id):
    LOG.debug("delete_vnf():vnf_id=%s", str(vnf_id))
    tackerclient(request).delete_vnf(vnf_id)


def delete_vnfd(request, vnfd_id):
    LOG.debug("delete_vnfd():vnfd_id=%s", str(vnfd_id))
    tackerclient(request).delete_vnfd(vnfd_id)


def create_vim(request, vim_arg):
    LOG.debug("create_vim(): vim_arg=%s", str(vim_arg))
    vim_instance = tackerclient(request).create_vim(body=vim_arg)
    return vim_instance


def get_vim(request, vim_id):
    LOG.debug("vim_get(): vim_id=%s", str(vim_id))
    vim_instance = tackerclient(request).show_vim(vim_id)
    return vim_instance


def delete_vim(request, vim_id):
    LOG.debug("delete_vim():vim_id=%s", str(vim_id))
    tackerclient(request).delete_vim(vim_id)


def vim_list(request, **params):
    LOG.debug("vim_list(): params=%s", params)
    vims = tackerclient(request).list_vims(**params).get('vims')
    return vims


def events_list(request, resource_id):
    params = {'resource_id': resource_id}
    events = tackerclient(request).list_events(**params).get('events')
    LOG.debug("events_list() params=%s events=%s l=%s", params, events,
              len(events))
    return events


def vnffg_list(request, **params):
    LOG.debug("vnffg_list(): params=%s", params)
    vnffgs = tackerclient(request).list_vnffgs(**params).get('vnffgs')
    return vnffgs


def vnffgd_list(request, **params):
    LOG.debug("vnffgd_list(): params=%s", params)
    vnffgds = tackerclient(request).list_vnffgds(**params).get('vnffgds')
    return vnffgds


def create_vnffgd(request, tosca_body=None, **params):
    LOG.debug("create_vnffgd(): params=%s", params)
    vnffgd_instance = tackerclient(request).create_vnffgd(body=tosca_body)
    return vnffgd_instance


def create_vnffg(request, vnffg_arg, **params):
    LOG.debug("create_vnffg(): vnf_arg=%s", str(vnffg_arg))
    vnffg_instance = tackerclient(request).create_vnffg(body=vnffg_arg)
    return vnffg_instance


def get_vnffgd(request, vnffgd_id):
    LOG.debug("vnffgd_get(): vnffgd_id=%s", str(vnffgd_id))
    vnffgd = tackerclient(request).show_vnffgd(vnffgd_id)
    return vnffgd


def get_vnffg(request, vnffg_id):
    LOG.debug("vnffg_get(): vnffg_id=%s", str(vnffg_id))
    vnffg_instance = tackerclient(request).show_vnffg(vnffg_id)
    return vnffg_instance


def delete_vnffg(request, vnffg_id):
    LOG.debug("delete_vnffg():vnffg_id=%s", str(vnffg_id))
    tackerclient(request).delete_vnffg(vnffg_id)


def delete_vnffgd(request, vnffgd_id):
    LOG.debug("delete_vnffgd():vnffgd_id=%s", str(vnffgd_id))
    tackerclient(request).delete_vnffgd(vnffgd_id)


def create_nsd(request, tosca_body=None, **params):
    LOG.debug("create_nsd(): params=%s", params)
    nsd_instance = tackerclient(request).create_nsd(body=tosca_body)
    return nsd_instance


def nsd_list(request, **params):
    LOG.debug("nsd_list(): params=%s", params)
    nsds = tackerclient(request).list_nsds(**params).get('nsds')
    return nsds


def get_nsd(request, nsd_id):
    LOG.debug("nsd_get(): nsd_id=%s", str(nsd_id))
    nsd = tackerclient(request).show_vnfd(nsd_id)
    return nsd


def delete_nsd(request, nsd_id):
    LOG.debug("delete_nsd():nsd_id=%s", str(nsd_id))
    tackerclient(request).delete_nsd(nsd_id)


def get_ns(request, ns_id):
    LOG.debug("ns_get(): ns_id=%s", str(ns_id))
    ns_instance = tackerclient(request).show_ns(ns_id)
    return ns_instance


def delete_ns(request, ns_id):
    LOG.debug("delete_ns():ns_id=%s", str(ns_id))
    tackerclient(request).delete_ns(ns_id)


def ns_list(request, **params):
    LOG.debug("ns_list(): params=%s", params)
    nss = tackerclient(request).list_nss(**params).get('nss')
    return nss


def create_ns(request, ns_arg, **params):
    LOG.debug("create_ns(): ns_arg=%s", str(ns_arg))
    ns_instance = tackerclient(request).create_ns(body=ns_arg)
    return ns_instance
