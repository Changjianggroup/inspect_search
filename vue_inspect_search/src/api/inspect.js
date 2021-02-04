import request from '../utils/request';

export function getInspectInfoList(queryParams) {
    return request({
        url: '/inspect/list',
        method: 'get',
        params: queryParams
    })
}